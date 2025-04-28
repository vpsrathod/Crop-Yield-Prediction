import pickle
from django.shortcuts import render

# Load models from pickle files//D:/Vishnu/Projects/crop prediction/crop_prediction/crop_prediction/prediction\model_files\crop_name_model.pkl
with open("D:/Vishnu/Projects/crop prediction/crop_prediction/crop_prediction/prediction/model_files/profit_model.pkl", "rb") as f:
    profit_model = pickle.load(f)

with open("D:/Vishnu/Projects/crop prediction/crop_prediction/crop_prediction/prediction/model_files/crop_name_model.pkl", "rb") as f:
    crop_name_model = pickle.load(f)

with open("D:/Vishnu/Projects/crop prediction/crop_prediction/crop_prediction/prediction/model_files/crop_type_model.pkl", "rb") as f:
    crop_type_model = pickle.load(f)

with open("D:/Vishnu/Projects/crop prediction/crop_prediction/crop_prediction/prediction/model_files/time_to_grow_model.pkl", "rb") as f:
    time_to_grow_model = pickle.load(f)


def predict_crop(request):
    if request.method == "POST":
        user_pH = float(request.POST.get("pH"))
        user_Nitrogen = float(request.POST.get("Nitrogen"))
        user_Phosphorus = float(request.POST.get("Phosphorus"))
        user_Potassium = float(request.POST.get("Potassium"))
        user_temperature = float(request.POST.get("Temperature"))

        user_data = [
            [user_pH, user_Nitrogen, user_Phosphorus, user_Potassium, user_temperature]
        ]
        user_profit_prediction = profit_model.predict(user_data)
        user_crop_type_prediction = crop_type_model.predict(user_data)
        user_crop_name_prediction = crop_name_model.predict(user_data)
        user_time_to_grow_prediction = time_to_grow_model.predict(user_data)

        # Context for rendering result.html
        context = {
            "predicted_crop_name": user_crop_name_prediction[0],
            "predicted_profit": user_profit_prediction[0],
            "predicted_crop_type": user_crop_type_prediction[0],
            "predicted_time_to_grow": user_time_to_grow_prediction[0],
        }

        return render(request, "prediction/result.html", context)

    return render(request, "prediction/form.html")

def home(request):
    return render(request,'prediction/home.html')

def about(request):
    return render(request, 'prediction/about.html')

def contact(request):
    return render(request, 'prediction/contact.html')
    
