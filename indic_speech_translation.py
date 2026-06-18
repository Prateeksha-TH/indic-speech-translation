import streamlit as st
import whisper
import torch
import numpy as np
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer, pipeline
import torchaudio
import tempfile
import os
from pathlib import Path
import warnings
warnings.filterwarnings('ignore')

# Page config
st.set_page_config(
    page_title="Indic Speech Translation",
    page_icon="🌍",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better UI
st.markdown("""
    <style>
    .main { padding: 2rem; }
    .stTabs [data-baseweb="tab-list"] button { font-size: 16px; }
    .header-title { font-size: 2.5rem; font-weight: bold; margin-bottom: 1rem; }
    .pipeline-box { 
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 1.5rem;
        border-radius: 10px;
        color: white;
        margin: 1rem 0;
    }
    .info-box {
        background-color: #f0f2f6;
        padding: 1rem;
        border-radius: 8px;
        margin: 1rem 0;
    }
    </style>
""", unsafe_allow_html=True)

# Initialize session state
if 'whisper_model' not in st.session_state:
    st.session_state.whisper_model = None
if 'translation_model' not in st.session_state:
    st.session_state.translation_model = None
if 'translation_tokenizer' not in st.session_state:
    st.session_state.translation_tokenizer = None
if 'tts_pipeline' not in st.session_state:
    st.session_state.tts_pipeline = None

# Sidebar Configuration
with st.sidebar:
    st.markdown("### 🔧 Models Configuration")
    
    # Device selection
    device = st.selectbox(
        "Device",
        options=["auto", "cpu", "cuda"],
        help="Select computation device"
    )
    
    if device == "auto":
        device = "cuda" if torch.cuda.is_available() else "cpu"
    
    # Whisper model selection
    whisper_size = st.selectbox(
        "Whisper ASR Model",
        options=["tiny", "base", "small", "medium", "large"],
        index=1,
        help="Larger models are more accurate but slower"
    )
    
    # Translation model info
    st.markdown("""
    **Neural Machine Translation**
    - Model: NLLB-200
    - Type: Sequence-to-Sequence
    """)
    
    # TTS model info
    st.markdown("""
    **Text-to-Speech**
    - Engine: Coqui TTS
    - Type: Multilingual
    """)
    
    st.divider()
    st.markdown("### 📊 Status")
    col1, col2 = st.columns(2)
    with col1:
        st.metric("Device", device.upper())
    with col2:
        st.metric("GPU Available", "Yes" if torch.cuda.is_available() else "No")

# Main content
st.markdown('<div class="header-title">🌍 Real-Time Indic Speech Translation</div>', unsafe_allow_html=True)

# Create two columns for input configuration
col1, col2 = st.columns(2)

with col1:
    source_lang = st.selectbox(
        "Source Language",
        options=["Hindi", "Tamil", "Telugu", "Kannada", "Bengali", "Marathi", "Gujarati", "Punjabi"],
        index=0,
        help="Select the language of your input speech"
    )

with col2:
    target_lang = st.selectbox(
        "Target Language",
        options=["English", "Hindi", "Tamil", "Telugu", "Kannada", "Bengali"],
        index=0,
        help="Select the language you want to translate to"
    )

# Pipeline info
st.markdown("""
<div class="pipeline-box">
    <b>Pipeline:</b> ASR → NMT → TTS
    <br>
    <small>Automatic Speech Recognition → Neural Machine Translation → Text-to-Speech</small>
</div>
""", unsafe_allow_html=True)

# Audio input
st.markdown("### 🎙️ Speech Audio")
audio_file = st.file_uploader(
    "Upload audio file or record speech",
    type=["wav", "mp3", "ogg", "flac", "m4a"],
    help="Supported formats: WAV, MP3, OGG, FLAC, M4A (Max 200MB)"
)

# Translate button
col1, col2, col3 = st.columns([1, 1, 2])
with col1:
    translate_btn = st.button("🎯 Translate Speech", use_container_width=True, type="primary")
with col2:
    clear_btn = st.button("🗑️ Clear", use_container_width=True)

if clear_btn:
    st.rerun()

# Processing
if translate_btn and audio_file is not None:
    with st.spinner("🔄 Loading models..."):
        try:
            # Load Whisper model
            if st.session_state.whisper_model is None:
                st.session_state.whisper_model = whisper.load_model(whisper_size, device=device)
            
            # Save uploaded file temporarily
            with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as tmp_file:
                tmp_file.write(audio_file.getbuffer())
                audio_path = tmp_file.name
            
            # Step 1: ASR (Speech to Text)
            with st.spinner("🎤 Transcribing speech..."):
                result = st.session_state.whisper_model.transcribe(audio_path)
                transcribed_text = result["text"]
            
            st.success("✅ Transcription complete!")
            
            with st.expander("📝 View Transcription", expanded=True):
                st.write(f"**{source_lang}:** {transcribed_text}")
            
            # Step 2: NMT (Translation)
            with st.spinner("🔄 Translating text..."):
                # Language code mapping for NLLB
                lang_codes = {
                    "Hindi": "hin_Deva",
                    "Tamil": "tam_Taml",
                    "Telugu": "tel_Telu",
                    "Kannada": "kan_Knda",
                    "Bengali": "ben_Beng",
                    "Marathi": "mar_Deva",
                    "Gujarati": "guj_Gujr",
                    "Punjabi": "pan_Guru",
                    "English": "eng_Latn"
                }
                
                src_lang = lang_codes.get(source_lang, "eng_Latn")
                tgt_lang = lang_codes.get(target_lang, "eng_Latn")
                
                try:
                    # Load translation model if not cached
                    if st.session_state.translation_model is None:
                        st.session_state.translation_model = AutoModelForSeq2SeqLM.from_pretrained(
                            "facebook/nllb-200-distilled-600M"
                        ).to(device)
                        st.session_state.translation_tokenizer = AutoTokenizer.from_pretrained(
                            "facebook/nllb-200-distilled-600M"
                        )
                    
                    # Translate
                    inputs = st.session_state.translation_tokenizer(
                        transcribed_text,
                        return_tensors="pt",
                        max_length=512,
                        truncation=True
                    ).to(device)
                    
                    with torch.no_grad():
                        outputs = st.session_state.translation_model.generate(
                            **inputs,
                            forced_bos_token_id=st.session_state.translation_tokenizer.convert_tokens_to_ids(tgt_lang),
                            max_length=512
                        )
                    
                    translated_text = st.session_state.translation_tokenizer.decode(
                        outputs[0],
                        skip_special_tokens=True
                    )
                    
                except Exception as e:
                    st.warning(f"Translation model loading issue: {str(e)}\nUsing original text for TTS.")
                    translated_text = transcribed_text
            
            st.success("✅ Translation complete!")
            
            with st.expander("🌐 View Translation", expanded=True):
                st.write(f"**{target_lang}:** {translated_text}")
            
            # Step 3: TTS (Text to Speech) - Optional
            with st.expander("🔊 Text-to-Speech (Optional)"):
                if st.button("Generate Audio from Translation"):
                    with st.spinner("🎵 Generating speech..."):
                        try:
                            # Try to use gTTS as fallback for TTS
                            from gtts import gTTS
                            
                            lang_map = {
                                "English": "en",
                                "Hindi": "hi",
                                "Tamil": "ta",
                                "Telugu": "te",
                                "Kannada": "kn",
                                "Bengali": "bn",
                                "Marathi": "mr",
                                "Gujarati": "gu",
                                "Punjabi": "pa"
                            }
                            
                            tts_lang = lang_map.get(target_lang, "en")
                            tts = gTTS(text=translated_text, lang=tts_lang, slow=False)
                            
                            with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as tmp_audio:
                                tts.save(tmp_audio.name)
                                audio_output_path = tmp_audio.name
                            
                            with open(audio_output_path, "rb") as audio_file_read:
                                st.audio(audio_file_read, format="audio/mp3")
                            
                            st.success("✅ Audio generated successfully!")
                            
                        except Exception as e:
                            st.info(f"Note: TTS requires additional setup. {str(e)}")
            
            # Cleanup
            if os.path.exists(audio_path):
                os.remove(audio_path)
            
        except Exception as e:
            st.error(f"❌ Error: {str(e)}")
            st.info("Make sure all required libraries are installed: `pip install openai-whisper transformers torch torchaudio gtts`")

# Instructions
with st.expander("📖 How to Use"):
    st.markdown("""
    1. **Select Languages**: Choose source (input) and target (output) languages
    2. **Upload Audio**: Drop an audio file or record speech
    3. **Translate**: Click the "Translate Speech" button
    4. **View Results**: See transcription, translation, and optional audio output
    
    **Supported Indic Languages:**
    - Hindi, Tamil, Telugu, Kannada, Bengali, Marathi, Gujarati, Punjabi
    
    **Pipeline Explanation:**
    - **ASR**: Converts speech to text using Whisper
    - **NMT**: Translates text using NLLB-200
    - **TTS**: Converts translated text back to speech (optional)
    """)

st.divider()
st.markdown("*Made with Streamlit • Powered by Whisper, NLLB-200, and gTTS*")
