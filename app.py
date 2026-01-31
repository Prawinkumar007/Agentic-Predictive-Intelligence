import pickle
import numpy as np
import os

def load_model(model_path):
    if not os.path.exists(model_path):
        print(f"Error: Pickle file not found at {model_path}")
        return None
    try:
        with open(model_path, "rb") as f:
            model = pickle.load(f)
        return model
    except Exception as e:
        print(f"Error loading pickle file: {e}")
        return None

def predict(model, features):
    try:
        features_array = np.array(features).reshape(1, -1)
        prediction = model.predict(features_array)[0]
        return prediction
    except Exception as e:
        print(f"Error during prediction: {e}")
        return None

def main():
    # Priority paths: Current directory, then Downloads folder
    dt_names = ["DecisionTreeRegressor.pkl", r"C:\Users\DELL\Downloads\DecisionTreeRegressor.pkl"]
    rf_names = ["random_forest_model.pkl", r"C:\Users\DELL\Downloads\random_forest_model (2).pkl"]

    print("--- Model Prediction Tool ---")
    print("1. Decision Tree")
    print("2. Random Forest")
    print("3. Enter custom model path")
    
    choice = input("Select model (1/2/3): ").strip()
    
    model_path = None
    if choice == '1':
        for path in dt_names:
            if os.path.exists(path):
                model_path = path
                break
        if not model_path: model_path = dt_names[0]
    elif choice == '2':
        for path in rf_names:
            if os.path.exists(path):
                model_path = path
                break
        if not model_path: model_path = rf_names[0]
    elif choice == '3':
        model_path = input("Enter full path to .pkl file: ").strip()
    else:
        print("Invalid choice.")
        return

    model = load_model(model_path)
    if model is None:
        return

    print("\nModel loaded successfully.")
    print("Enter the 8 feature values (separated by commas, spaces, or tabs):")
    # Example: 380, 95, 0, 228, 0, 932, 594, 365
    features_input = input("Features: ").strip()
    
    try:
        # Handle multiple delimiters (commas, spaces, tabs)
        import re
        features = [float(x) for x in re.split(r'[,\s\t]+', features_input) if x]
        
        if len(features) != 8:
            print(f"Warning: Expected 8 features, got {len(features)}. Prediction might fail.")
            
        prediction = predict(model, features)
        if prediction is not None:
            print(f"\n🎯 Predicted Target: {prediction:.4f}")
            
    except ValueError:
        print("Error: Please enter valid numeric values.")

if __name__ == "__main__":
    main()


