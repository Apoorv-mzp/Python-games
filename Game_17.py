# ==========================================
# MINI HOSPITAL MANAGEMENT SYSTEM 🏥
# ==========================================

print("==========================================")
print("......MINI HOSPITAL MANAGEMENT SYSTEM 🏥......")
print("==========================================")

# ------------------------------------------
# Patient Details
# ------------------------------------------

patient_name = input("\nEnter Patient Name : ")

age = int(input("Enter Patient Age : "))

disease = input("Enter Disease Name : ").lower()

# ------------------------------------------
# Emergency Check
# ------------------------------------------

emergency = input("Is it an Emergency? (yes/no) : ").lower()

# ------------------------------------------
# Doctor Assignment
# ------------------------------------------

if disease == "fever":
    doctor = "General Doctor"
    doctor_fee = 500

elif disease == "heart":
    doctor = "Cardiologist"
    doctor_fee = 2000

elif disease == "bone":
    doctor = "Orthopedic"
    doctor_fee = 1500

elif disease == "skin":
    doctor = "Dermatologist"
    doctor_fee = 1200

else:
    doctor = "General Doctor"
    doctor_fee = 500

# ------------------------------------------
# Priority Check
# ------------------------------------------

if age >= 60:
    priority = "Senior Citizen Priority"

else:
    priority = "Normal Priority"

# ------------------------------------------
# Emergency Message
# ------------------------------------------

if emergency == "yes":
    emergency_status = "Immediate Admission Required do as soon as possible!"

else:
    emergency_status = "Normal Admission"

# ------------------------------------------
# Room Selection
# ------------------------------------------

print("\nSelect Room Type")
print("1. General Ward")
print("2. Private Room")
print("3. ICU")

room_choice = int(input("Enter Your Choice : "))

# ------------------------------------------
# Room Charges
# ------------------------------------------

if room_choice == 1:
    room_type = "General Ward"
    room_charge = 1000

elif room_choice == 2:
    room_type = "Private Room"
    room_charge = 3000

elif room_choice == 3:
    room_type = "ICU"
    room_charge = 7000

else:
    room_type = "General Ward"
    room_charge = 1000
    print("Invalid Choice! General Ward Selected.")

# ------------------------------------------
# Number of Days
# ------------------------------------------

days = int(input("\nEnter Number of Days Admitted : "))

# ------------------------------------------
# Medicine Charges
# ------------------------------------------

medicine_charge = int(input("Enter Medicine Charges : ₹"))

# ------------------------------------------
# Total Bill Calculation
# ------------------------------------------

room_total = room_charge * days

total_bill = doctor_fee + room_total + medicine_charge

# ------------------------------------------
# Senior Citizen Discount
# ------------------------------------------

discount = 0

if age >= 60:
    discount = total_bill * 0.10

final_bill = total_bill - discount

# ------------------------------------------
# Final Report
# ------------------------------------------

print("\n")
print("==========================================")
print("          HOSPITAL RECEIPT 🏥")
print("==========================================")

print("Patient Name      :", patient_name)

print("Age               :", age)

print("Disease           :", disease.title())

print("Assigned Doctor   :", doctor)

print("Priority Status   :", priority)

print("Emergency Status  :", emergency_status)

print("Room Type         :", room_type)

print("Days Admitted     :", days)

print("------------------------------------------")

print("Doctor Fee        : ₹", doctor_fee)

print("Room Charges      : ₹", room_total)

print("Medicine Charges  : ₹", medicine_charge)

print("------------------------------------------")

print("Total Bill        : ₹", total_bill)

print("Discount          : ₹", round(discount, 2))

print("------------------------------------------")

print("Final Bill        : ₹", round(final_bill, 2))

print("==========================================")

# ------------------------------------------
# Health Advice
# ------------------------------------------

print("\n----------- HEALTH ADVICE -----------")

if disease == "fever":
    print("🌡 Drink more water and take rest.")

elif disease == "heart":
    print("❤️ Avoid stress and oily food.")

elif disease == "bone":
    print("🦴 Take calcium-rich diet.")

elif disease == "skin":
    print("🧴 Keep your skin clean and hydrated.")

elif disease == "Hair":
    print("🧑🏻‍🦲 Always use oil and shampo.")

else:
    print("💊 Follow doctor's instructions properly.")

# ------------------------------------------
# Final Message
# ------------------------------------------

print("\n==========================================")

if emergency == "yes":
    print("🚑 Emergency Team Activated!")

print("🙏 Thank You for Visiting Our Hospital")

print("==========================================")