# 🌍 Real-Time Indic Speech Translation

A Streamlit application for translating speech between Indian languages using cutting-edge AI models.

## Features

✅ **Automatic Speech Recognition (ASR)** - Whisper  
✅ **Neural Machine Translation (NMT)** - NLLB-200  
✅ **Text-to-Speech (TTS)** - gTTS  
✅ **Support for Multiple Indic Languages** - Hindi, Tamil, Telugu, Kannada, Bengali, Marathi, Gujarati, Punjabi  
✅ **Real-time Processing** - Fast inference with GPU support  
✅ **User-Friendly Interface** - Modern Streamlit UI  

## System Requirements

- **Python**: 3.8 or higher
- **RAM**: Minimum 8GB (16GB recommended for better performance)
- **Storage**: At least 5GB free space (for model downloads)
- **GPU**: NVIDIA GPU with CUDA support (optional but recommended for faster processing)

## Installation

### 1. Clone or download this repository

```bash
git clone <repo-url>
cd indic-speech-translation
```

### 2. Create a virtual environment (recommended)

**On Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**On macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

This will install:
- **Streamlit** - Web interface
- **Whisper** - Speech recognition
- **Transformers** - NLP models
- **PyTorch** - Deep learning framework
- **gTTS** - Text-to-speech synthesis

### 4. (Optional) Install CUDA for GPU acceleration

If you have an NVIDIA GPU and want faster processing:

```bash
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
```

## Usage

### Running the App

```bash
streamlit run indic_speech_translation.py
```

The app will open at `http://localhost:8501`

### Step-by-Step Guide

1. **Select Languages**
   - Choose your source language (language of input audio)
   - Choose your target language (language for output)

2. **Upload Audio**
   - Drag and drop an audio file, or click "Browse files"
   - Supported formats: WAV, MP3, OGG, FLAC, M4A
   - Max file size: 200MB

3. **Translate**
   - Click the "🎯 Translate Speech" button
   - Wait for processing:
     - ASR: Converts speech to text
     - NMT: Translates text
     - TTS: (Optional) Converts text back to speech

4. **View Results**
   - See the transcription in the source language
   - See the translation in the target language
   - Listen to the translated speech (optional)

## Supported Languages

**Source & Target Languages:**
- Hindi (hin_Deva)
- Tamil (tam_Taml)
- Telugu (tel_Telu)
- Kannada (kan_Knda)
- Bengali (ben_Beng)
- Marathi (mar_Deva)
- Gujarati (guj_Gujr)
- Punjabi (pan_Guru)
- English (eng_Latn)

## Models Used

### 1. **Whisper (OpenAI)**
- Automatic Speech Recognition
- Available sizes: tiny, base, small, medium, large
- Better accuracy with larger models, but slower

### 2. **NLLB-200 (Meta)**
- Neural Machine Translation
- Supports 200+ languages
- Model: facebook/nllb-200-distilled-600M (lightweight)

### 3. **gTTS (Google Text-to-Speech)**
- Text-to-Speech synthesis
- Free and online service
- Supports multiple languages

## Performance Tips

- **First Run**: The first time you run the app, models will be downloaded (may take 5-10 minutes depending on internet speed)
- **GPU Usage**: Use CUDA for 5-10x faster processing
- **Model Size**: Start with "base" Whisper model for balance between speed and accuracy
- **Batch Processing**: Upload multiple files one at a time for best results

## Troubleshooting

### Issue: "CUDA out of memory"
**Solution**: 
- Use smaller Whisper model (tiny or base)
- Reduce audio file length
- Close other applications using GPU

### Issue: "Models not downloading"
**Solution**:
- Check internet connection
- Manually download models:
  ```bash
  python -c "import whisper; whisper.load_model('base')"
  ```

### Issue: "Module not found"
**Solution**:
```bash
pip install -r requirements.txt --upgrade
```

### Issue: "No module named 'torch'"
**Solution**:
```bash
pip install torch torchaudio transformers
```

## Configuration

Edit the sidebar in the app to:
- Select computation device (CPU/GPU)
- Choose Whisper model size
- Monitor resource usage

## Deployment

### Deploy to Streamlit Cloud (Free)

1. Push code to GitHub
2. Go to [Streamlit Cloud](https://streamlit.io/cloud)
3. Click "New app" and connect your repository
4. Set main file to `indic_speech_translation.py`

### Deploy to Hugging Face Spaces

1. Create a repo on [Hugging Face](https://huggingface.co/spaces)
2. Push code with `app.py` as the filename
3. Select "Streamlit" as the SDK

## License

This project uses:
- Whisper (OpenAI) - MIT License
- NLLB-200 (Meta) - CC-BY-NC 4.0
- gTTS - MIT License

## Contributing

Contributions are welcome! Feel free to submit issues or pull requests.

## Support

For issues or questions:
- Check the troubleshooting section
- Review Streamlit documentation: https://docs.streamlit.io/
- Whisper docs: https://github.com/openai/whisper
- NLLB docs: https://huggingface.co/facebook/nllb-200-distilled-600M

---

**Made with ❤️ for Indic language speakers**
