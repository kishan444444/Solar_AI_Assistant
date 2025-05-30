# ☀️ Solar Rooftop Analysis Tool

A Streamlit app combining basic computer vision and LLM AI to analyze rooftop images for solar panel feasibility. Upload rooftop images and location info to get an edge-detection preview and an AI-generated report covering technology, installation, cost, regulations, and market trends.

---

## 🚀 Setup

1. Clone repo (if any):  
   `git clone <repo_url> && cd <repo_dir>`

2. Create & activate virtual env:  
   - Windows: conda create -p venv python=3.10 
   -

3. Install dependencies:  
   `pip install -r requirement.txt

4. Set OpenRouter API key:  
   -`set OPENROUTER_API_KEY="your_key"`  in .env file
   

5. Run app:  
   `streamlit run app.py`

---

## 🛠 Features

- Upload rooftop images (JPG/PNG/JPEG)  
- edge detection visualization  
- Simulate and adjust usable rooftop area (m²)  
- Input location and electricity cost per kWh  
- AI-generated solar panel feasibility report via OpenRouter LLM
- accurate solar potential assessments 
- installation recommendations
- ROI estimates for both homeowners and solar professionals.

---

## 🔮 Use Cases

- Homeowners assessing solar potential 
- solar professionals assessing solar potential  


---

## ⚙️ Minimal Support Files

**logger.py**  
**exception.py**


## 🚀 Future Improvements

- Deep learning for accurate rooftop segmentation
- Shading and sun path analysis integration
- Financial modeling with local incentives
- UI enhancements with sliders and tabs
- Streaming LLM responses and Q&A features





