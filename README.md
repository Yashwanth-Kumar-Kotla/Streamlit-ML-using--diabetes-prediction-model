# 🩺 Diabetes Prediction using Machine Learning

An intelligent web application that leverages machine learning to predict the likelihood of diabetes based on key health metrics. Built with Python and deployed using Streamlit for an intuitive, interactive user experience.

## 🌟 Live Demo

**Try it now:** [Diabetes Prediction App](https://diabetespredictionusing.streamlit.app/)

Experience real-time diabetes risk assessment with just a few health parameters!

## 📋 Overview

Diabetes is one of the most prevalent chronic diseases worldwide, affecting millions of people. Early detection and risk assessment are crucial for effective management and prevention. This project combines the power of machine learning with an accessible web interface to help identify potential diabetes cases based on clinical measurements.

The application uses a trained Support Vector Machine (SVM) model to analyze health indicators and provide instant predictions, making preliminary diabetes screening more accessible to everyone.

## ✨ Features

- **Instant Predictions**: Get real-time diabetes risk assessment based on input health metrics
- **User-Friendly Interface**: Clean, intuitive Streamlit-based web application
- **Machine Learning Powered**: Utilizes SVM classifier trained on diabetes dataset
- **Accessible Anywhere**: Cloud-deployed application accessible from any device
- **Educational Value**: Understand which health factors influence diabetes risk

## 🔬 How It Works

The prediction model analyzes eight key health parameters:

1. **Pregnancies**: Number of times pregnant
2. **Glucose**: Plasma glucose concentration
3. **Blood Pressure**: Diastolic blood pressure (mm Hg)
4. **Skin Thickness**: Triceps skin fold thickness (mm)
5. **Insulin**: 2-Hour serum insulin (mu U/ml)
6. **BMI**: Body mass index (weight in kg/(height in m)^2)
7. **Diabetes Pedigree Function**: Genetic factor indicating diabetes history
8. **Age**: Age in years

Based on these inputs, the model predicts whether an individual is diabetic or non-diabetic.

## 🛠️ Technology Stack

- **Python**: Core programming language
- **Streamlit**: Web application framework
- **Scikit-learn**: Machine learning library for model training
- **Pandas & NumPy**: Data manipulation and numerical computing
- **Pickle**: Model serialization

## 📂 Project Structure

```
├── Diabetes Web App.py                    # Main Streamlit application
├── Predictive system.py                    # Standalone prediction script
├── Diabetes Prediction using Machine Learning with Python.ipynb  # Model training notebook
├── trained_model.sav                       # Serialized trained model
├── diabetes.csv                            # Dataset used for training
├── requirements.txt                        # Python dependencies
└── .devcontainer/                          # Development container configuration
```

## 🚀 Getting Started

### Prerequisites

- Python 3.7 or higher
- pip package manager

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/Yashwanth-Kumar-Kotla/Streamlit-ML-using--diabetes-prediction-model.git
   cd Streamlit-ML-using--diabetes-prediction-model
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**
   ```bash
   streamlit run "Diabetes Web App.py"
   ```

4. **Access the app**
   - The application will automatically open in your default browser
   - If not, navigate to `http://localhost:8501`

## 💡 Usage

1. Open the web application (either locally or via the [live demo](https://diabetespredictionusing.streamlit.app/))
2. Enter the required health parameters in the input fields
3. Click the "Predict" button
4. View your diabetes risk assessment instantly

## 📊 Model Performance

The model has been trained using the Pima Indians Diabetes Database, a well-known dataset in the machine learning community. The Support Vector Machine classifier provides reliable predictions based on the correlation between health metrics and diabetes occurrence.

For detailed model training and evaluation, refer to the Jupyter notebook included in the repository.

## 🎯 Use Cases

- **Personal Health Assessment**: Quick preliminary screening for diabetes risk
- **Educational Tool**: Learning resource for understanding diabetes risk factors
- **Healthcare Support**: Supplementary tool for healthcare professionals (not a replacement for medical diagnosis)
- **Research & Development**: Base project for exploring ML in healthcare applications

## ⚠️ Disclaimer

This application is designed for educational and informational purposes only. It should **NOT** be used as a substitute for professional medical advice, diagnosis, or treatment. Always consult with a qualified healthcare provider for medical concerns and before making any health-related decisions.

## 🤝 Contributing

Contributions are welcome! If you'd like to improve this project:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is open source and available for educational and research purposes.

## 👤 Author

**Yashwanth Kumar Kotla**

- GitHub: [@Yashwanth-Kumar-Kotla](https://github.com/Yashwanth-Kumar-Kotla)

## 🙏 Acknowledgments

- Dataset: Pima Indians Diabetes Database
- Streamlit team for the excellent framework
- The open-source community for continuous inspiration

---

⭐ If you find this project helpful, please consider giving it a star!

**Live Application**: [https://diabetespredictionusing.streamlit.app/](https://diabetespredictionusing.streamlit.app/)
