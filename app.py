import streamlit as st
from PIL import Image
import requests
import os
import sys
import re
import cv2
import numpy as np
import random
from logger import logging
from exception import customexception

api_key = os.getenv("OPENROUTER_API_KEY")

class solar_rooftop_analysis_app:
    def __init__(self):
        pass

    def detect_edges(self,pil_image):
        """Convert image to grayscale and apply Canny edge detection."""
        image_np = np.array(pil_image.convert("L"))
        edges = cv2.Canny(image_np, 50, 150)
        return Image.fromarray(edges)

    def simulate_usable_area(self):
        """Simulate usable rooftop area in m²."""
        return round(random.uniform(40, 100), 2)
    
    
    def run(self):
        try:
            st.set_page_config(page_title="Solar Rooftop Analysis Tool", layout="wide")
            st.title("☀️ Solar Rooftop Analysis Tool")

            uploaded_files = st.file_uploader("Upload one or more rooftop satellite images", type=["jpg", "png", "jpeg"], accept_multiple_files=True)
            location = st.text_input("Enter your location (City, Country)")
            electricity_cost = st.number_input("Electricity cost (per kWh in $)", min_value=0.0, value=0.12)

            if uploaded_files and location:
                for idx, uploaded_file in enumerate(uploaded_files):
                    st.markdown("---")
                    st.subheader(f"📸 Analyzing Image: {uploaded_file.name}")
                    image = Image.open(uploaded_file)
                    st.image(image, caption="Uploaded Rooftop Image", use_column_width=True)

                    # Edge Detection
                    st.subheader("🧠 Vision AI (Edge Detection)")
                    edge_image = self.detect_edges(image)
                    st.image(edge_image, caption="Detected Edges", use_column_width=True)

                    # Simulated Usable Area
                    simulated_area = self.simulate_usable_area()
                    st.success(f"🧱 Simulated usable rooftop area: **{simulated_area} m²**")

                    usable_area = st.number_input(
                        f"Adjust usable rooftop area for {uploaded_file.name} (in m²)",
                        min_value=1.0, value=simulated_area, key=f"area_{idx}"
                    )

                    # LLM Prompt
                    prompt = f"""
                    Analyze the following rooftop:
                    - Location: {location}
                    - Usable Rooftop Area: {usable_area} square meters
                    - Electricity Cost: ${electricity_cost} per kWh

                    Please provide a detailed, bullet-point report including:

                    1. **Solar Panel Technology**
                    - Recommended panel types (e.g., monocrystalline, polycrystalline)
                    - Typical efficiencies and technical specifications

                    2. **Installation Process**
                    - Suitable mounting methods for this rooftop
                    - Electrical system considerations and necessary permits

                    3. **Maintenance Requirements**
                    - Best practices for monitoring and cleaning
                    - Warranty recommendations and service intervals

                    4. **Cost & ROI Analysis**
                    - Estimated installation costs in USD and INR
                    - Available incentives, subsidies, or rebates
                    - Payback period and ROI projections
                    - Estimated savings over 25 years

                    5. **Industry Regulations**
                    - Relevant safety codes and standards
                    - Net metering policies applicable to the location

                    6. **Market Trends**
                    - Recent technological advances impacting solar installations
                    - Adoption rates or market insights relevant to this region

                    Please keep the tone professional and the formatting clear with bullet points for easy readability.
                    """

                    st.subheader("LLM Response")
                    with st.spinner("Analyzing with LLM..."):
                        headers = {
                            "Authorization": f"Bearer {api_key}",
                            "Content-Type": "application/json"
                        }
                        data = {
                            "model": "mistralai/mixtral-8x7b-instruct",
                            "messages": [{"role": "user", "content": prompt}]
                        }

                        response = requests.post("https://openrouter.ai/api/v1/chat/completions", headers=headers, json=data)

                        if response.status_code == 200:
                            try:
                                result = response.json()
                                content = result['choices'][0]['message']['content']
                                st.markdown("#### ✅ LLM Result:")
                                st.markdown(content)

                            except Exception as e:
                                st.error(f"Error parsing LLM response: {e}")
                        else:
                            st.error(f"LLM API Error ({response.status_code}): {response.text}")
            else:
                st.info("Please upload rooftop images and enter location to proceed.")
        except Exception as e:
            logging.info("Exception occurred in app")
            raise customexception(e, sys)

if __name__ == "__main__":
    app = solar_rooftop_analysis_app()
    app.run()