# ============================================================
#   SPAM DETECTOR — Built From Scratch Using NLP
#   Uses everything from the lecture:
#   Tokenization → Normalization → Stopwords → Lemmatization
#   → TF-IDF → Feature Selection → Model → Evaluation
#
#   DATASET: Download from Kaggle
#   https://www.kaggle.com/datasets/uciml/sms-spam-collection-dataset
#   File name: spam.csv
#   Put spam.csv in the same folder as this script
#
#   INSTALL:
#   pip install nltk scikit-learn pandas matplotlib seaborn imbalanced-learn
# ============================================================

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import re
import string
import warnings
warnings.filterwarnings('ignore')

import nltk
# nltk.download('punkt',          quiet=True)
# nltk.download('punkt_tab',      quiet=True)
# nltk.download('stopwords',      quiet=True)
# nltk.download('wordnet',        quiet=True)
# nltk.download('omw-1.4',        quiet=True)

from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_selection import SelectKBest, chi2
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.linear_model import LogisticRegression
from sklearn.svm import LinearSVC
from sklearn.metrics import (accuracy_score, precision_score,
                             recall_score, f1_score,
                             classification_report, confusion_matrix,
                             roc_auc_score, roc_curve)
from imblearn.over_sampling import SMOTE


# ============================================================
# STEP 1: LOAD DATA
# ============================================================

print("=" * 60)
print("STEP 1: LOADING DATA")
print("=" * 60)

# ── Try loading real dataset first ────────────────────────
try:
    df = pd.read_csv('spam.csv', encoding='latin-1')

    # Keep only useful columns
    df = df[['v1', 'v2']]
    df.columns = ['label', 'text']
    print(f"  Loaded real dataset: {len(df)} emails")

except FileNotFoundError:
    print("  spam.csv not found — using built-in demo dataset")
    print("  Download real data from:")
    print("  https://www.kaggle.com/datasets/uciml/sms-spam-collection-dataset")
    print()

    # Built-in demo dataset (100 samples to show full pipeline)
    spam_emails = [

        "We reviewed your CV and want to offer you $80/hr remote role.",
        "Hiring now! No experience required. Earn $300 daily from home.",
        "A top firm shortlisted you. Confirm your slot before it fills.",
        "Work 2 hours a day and earn a full-time salary. Apply here.",
        "Remote data entry job. $25 per form. No experience required.",
        "Our recruiter found your profile. Interview slots filling fast.",
        "Congratulations! You passed the screening. Confirm your offer.",
        "Earn $150/hour as a mystery shopper. Register free today.",
        "Part-time online tutor needed. $90/hr. Flexible hours daily.",
        "Urgent hiring: social media manager. $5000/month. Apply now!",
        "You are shortlisted for a Google remote role. Confirm today.",
        "We pay $200 per Instagram post. Apply to be our brand rep.",
        "Freelance writer needed. $500 per article. No deadline stress.",
        "Recruitment agency found 5 matches for your profile. View now.",
        "Job offer waiting in your inbox. Confirm before someone else takes it.",
     
        # ── Fake Subscription / Billing ──
        "Your free trial ends tonight. Upgrade now to keep all features.",
        "Invoice attached. Payment of $299 due today. Avoid suspension.",
        "Your streaming plan auto-renews at $49.99. Cancel if needed.",
        "We could not process your payment. Update card to stay active.",
        "Your cloud storage subscription failed. Re-enter billing info.",
        "You have an outstanding balance of $89. Pay now to avoid fee.",
        "Membership fee of $199 will be charged tomorrow automatically.",
        "Your domain expires in 48 hours. Renew now to avoid losing it.",
        "Annual plan renewal failed. Your access will end in 12 hours.",
        "Billing issue detected on your account. Click to fix it now.",
     
        # ── Fake Delivery / Shipping ──
        "Your parcel could not be delivered. Pay $1.99 to reschedule.",
        "DHL notice: package held at customs. Click to release it now.",
        "Delivery failed: wrong address. Update details to retry delivery.",
        "Your order is stuck in transit. Confirm address to proceed.",
        "FedEx alert: your shipment requires action. Click link below.",
        "Customs duty of $4.50 required before your parcel is released.",
        "Your package was returned. Rebook delivery for just $2 now.",
        "Postal service: item undeliverable. Provide correct info here.",
        "Tracking shows your item is delayed. Pay fee to expedite it.",
        "Your Amazon return was rejected. Claim refund by clicking here.",
     
        # ── Crypto / NFT / Investment ──
        "Bitcoin will hit $200K. Buy now before the big surge happens.",
        "Exclusive NFT drop only for selected wallets. Mint yours now.",
        "Earn 20% weekly on your crypto. Fully automated trading bot.",
        "DeFi platform gives 500% APY. Join before slots close today.",
        "Elon Musk backed this coin. Early investors already up 400%.",
        "New ICO launching tomorrow. Get in early before public listing.",
        "Copy our expert traders automatically. Earn without any effort.",
        "Your crypto wallet has an unclaimed airdrop. Connect to claim.",
        "Staking rewards of 80% monthly. No lock-in period required.",
        "Our AI trades crypto for you. Guaranteed 15% daily profit.",
        "This altcoin is about to 100x. Buy before the big announcement.",
        "Presale ends in 6 hours. Last chance to buy at lowest price.",
     
        # ── Fake Government / Legal ──
        "IRS notice: unpaid taxes detected. Pay immediately to avoid arrest.",
        "Government stimulus check of $1,400 is unclaimed in your name.",
        "Legal action will be taken if you do not respond within 24 hours.",
        "Your social security benefits are on hold. Verify details now.",
        "Police department: warrant issued against you. Call this number.",
        "Ministry of Finance: your refund of $780 is pending. Apply now.",
        "Court notice: failure to respond may result in imprisonment.",
        "You are eligible for a pandemic relief grant. Apply before cutoff.",
        "FBI cybercrime unit has flagged your IP. Call to clear your name.",
        "Your driving record shows violations. Pay fine to avoid license loss.",
     
        # ── Fake Tech Support ──
        "Your Windows license has expired. Call support now to renew.",
        "Virus detected on your device. Download our cleaner instantly.",
        "Your router has been hacked. Reset it by calling our helpline.",
        "Microsoft detected malware on your PC. Act before data is lost.",
        "Your browser is outdated and vulnerable. Update now for safety.",
        "Warning: your phone is being tracked. Install our VPN for free.",
        "Apple support: your iCloud was accessed from an unknown device.",
        "Your antivirus has expired. Renew now for continuous protection.",
        "Trojan found in your system. Call toll-free to remove it now.",
        "Click here to speed up your slow computer in under 2 minutes.",
     
        # ── Fake Real Estate / Rental ──
        "Luxury apartment available. No credit check. Move in today!",
        "Earn passive income from real estate. No money down required.",
        "Buy this plot before price doubles next month. Only 3 left.",
        "Rent to own homes available in your city. Zero down payment.",
        "Foreclosed homes at 60% below market. Grab yours before gone.",
        "Property investment seminar. Attend free and earn in 30 days.",
     
        # ── Fake Charity / Emotional ──
        "Hungry children need your help. Donate $5 to feed them today.",
        "Disaster victims urgently need funds. Give now to help them.",
        "Your small donation can save a life. Click to contribute now.",
        "Help orphans this Ramadan. Every dollar goes directly to them.",
        "Animal rescue needs urgent funding. Donate before shelter closes.",
     
        # ── Relationship / Social Engineering ──
        "I found your contact online. I am a widow with inheritance to share.",
        "I am a diplomat with $15 million to transfer. I need your help.",
        "My late husband left funds. I need trusted person to help claim it.",
        "I am stuck abroad and need $500 urgently. Please help me now.",
        "A business partner needs you urgently. Reply to this message.",
        "Your long-lost relative left you an inheritance. Contact us now.",
        "Military officer has gold bars. Needs partner to claim them abroad.",
     
        # ── Misc Unique Spam ──
        "Your horoscope says money is coming. Open this to find out.",
        "This one food destroys belly fat. Doctors are now removing posts.",
        "Bill Gates is giving away money. Share this and receive $1000.",
        "Forward this to 10 people and get free data for 30 days now.",
        "Hidden camera footage found. See if you are in this video.",
        "You were tagged in a photo. Click here to see who tagged you.",
        "WhatsApp is going paid. Send this message to stay activated.",
        "Warning: your WhatsApp will be deleted in 24 hours. Tap here.",
        "Your phone number was found in a data breach. Secure it now.",
        "Click to unlock the secret menu on your streaming platform.",
        "This productivity app pays you $2 per hour while you use it.",
        "Watch this video before it gets banned. Share with everyone.",
        "Your dream car is available at 90% off. Only 2 units remaining.",
        "Receive a monthly allowance just for sharing your opinion online.",
        "Access any blocked website for free. Download our VPN proxy.",

        # Prize / Lottery / Giveaway
        "Congratulations! You won a free iPhone. Click here to claim now!",
        "WINNER!! You have been selected for a $1000 prize. Call now!",
        "Free entry into our weekly competition. Text WIN to 87121",
        "You have won a lottery. Send your details to claim your prize.",
        "You are selected as a winner. Claim your free gift card today!",
        "Win a holiday to Maldives. Enter now at our website!",
        "Your mobile number won our monthly draw. Reply YES to claim.",
        "Congratulations! You are our lucky winner this month. Claim now!",
        "You have been chosen for a $500 Amazon gift card. Click here.",
        "You won a brand new Samsung TV. Click to confirm your delivery.",
        "Final draw winner: YOU! Claim your cash prize before it expires.",
        "We are pleased to inform you that you have won 1 million dollars.",
        "Your email was randomly selected. Claim your iPad Pro today!",
        "Exclusive prize draw! You qualify. Confirm now to receive it.",
        "Lucky you! You are among 5 winners selected this week. Claim!",
        "You have been awarded a $250 Walmart voucher. Redeem today!",
        "Spin the wheel and win! You already have a guaranteed prize.",
        "Your number is the jackpot winner. Send details to claim.",
        "Hurry! Your prize expires in 24 hours. Claim immediately.",
        "We tried to reach you about your prize. Please respond ASAP.",
     
        # Financial Scams
        "Get free money now! Limited time offer. Act fast!",
        "Double your investment in 24 hours. Guaranteed returns!",
        "Earn money fast! Join our network marketing team today.",
        "Make $5000 per week working from home. No experience needed!",
        "Cheap loans available now. Apply with no credit check!",
        "You qualify for government tax refund. Claim $500 now!",
        "Invest $100 today and get $1000 back in 7 days. Risk free!",
        "Passive income opportunity. Earn while you sleep. Join now!",
        "Top traders earn $10,000 monthly. Start with just $50 today.",
        "Get rich quick! Proven method earns thousands per week.",
        "No investment needed. Just refer friends and earn $200 daily.",
        "Government grant available for you. Apply before deadline today.",
        "Your credit score qualifies you for a $10,000 instant loan.",
        "Binary trading made easy. Start earning from tomorrow morning.",
        "Crypto investment returns 300% in 30 days. Sign up today!",
        "We will pay your bills if you complete this short survey now.",
        "Financial freedom in 90 days. Proven plan. Start immediately.",
        "Earn $500 daily doing simple tasks online. No skills needed.",
        "Send $50 to receive $500 back. Verified by thousands of users.",
        "Work from home and earn six figures. Training provided free.",
     
        # Health / Medical
        "Amazing weight loss pill. Lose 30lbs in 30 days guaranteed!",
        "Buy cheap medicine online. No prescription needed. Order now!",
        "Cure diabetes naturally in 7 days with this secret formula.",
        "Doctors hate this one trick that burns belly fat overnight.",
        "Lose weight without exercise. New pill approved by experts.",
        "Enlarge and improve performance naturally. Order discreetly.",
        "Herbal supplement reverses aging. Look 20 years younger now.",
        "100% natural cure for high blood pressure. No side effects.",
        "This detox tea flushes toxins and helps you lose 10kg fast.",
        "No prescription? No problem. Order medication directly online.",
        "New supplement boosts brain power by 200%. Limited stock left.",
        "Clinically proven fat burner. Lose 5 inches in just 2 weeks.",
        "Stop hair loss forever with our exclusive herbal treatment.",
        "Your pain can end today. Order our miracle gel without script.",
        "Sleep better tonight with this natural remedy. Order online.",
     
        # Phishing / Account Threats
        "Urgent! Your account will be suspended. Click here immediately.",
        "Your bank account is at risk. Verify your details immediately.",
        "Final notice: Your package is waiting. Click to reschedule delivery.",
        "Security alert! Suspicious login detected. Verify your account now.",
        "Your PayPal account has been limited. Update your information now.",
        "Important: Your Netflix subscription failed. Update billing here.",
        "Your Google account will be deactivated. Click to restore access.",
        "We have detected unusual activity. Confirm your identity now.",
        "Your Apple ID has been locked. Unlock it by clicking here.",
        "URGENT: Your password will expire in 24 hours. Reset now.",
        "Your Amazon account is on hold. Verify your payment method.",
        "Tax authority notice: You owe money. Pay immediately to avoid penalty.",
        "Your email storage is full. Click here to upgrade for free.",
        "Action required: Your card was used in an unauthorized transaction.",
        "System alert: Your computer has been infected. Call support now.",
        "Your Microsoft account shows suspicious activity. Verify now.",
        "Bank alert: Your PIN was entered incorrectly 3 times. Click here.",
        "Last warning before we close your account permanently today.",
        "Your social security number has been compromised. Act now!",
        "Click here to prevent unauthorized access to your account today.",
     
        # Gambling / Casino
        "Best casino bonus online. Get $200 free today. Sign up now!",
        "Win big at our online casino! 500 free spins waiting for you.",
        "Top rated sports betting site. Bet $10 get $50 bonus today.",
        "New online poker room. Play free and win real money tonight.",
        "Bet and win daily! Guaranteed cashback on every losing bet.",
        "Join our casino and get 100% match on your first deposit today.",
        "Play slots for free. No download needed. Win real prizes now.",
        "Exclusive VIP casino invite. Claim your bonus before midnight.",
     
        # Misc Spam
        "FREE ringtone! Text MUSIC to 87066. Only $3/week.",
        "Debt problems? We can help. Call our free helpline today.",
        "Exclusive offer for you only. Limited stock available now!",
        "Hot deal alert! 90% off on all products today only. Shop now!",
        "Your opinion matters. Complete survey and earn $100 gift card.",
        "Cheap designer handbags. Replica brands at 99% discount today.",
        "Flash sale ends in 1 hour. Grab it before everyone else does.",
        "You have been pre-approved for an exclusive membership today.",
        "Claim your complimentary vacation package now. Limited time.",
        "We are giving away free laptops. Click here to get yours now.",
        "Blocked on WhatsApp? Use this trick to see anyone's status.",
        "Grow your Instagram followers to 10,000 overnight. Click here.",
        "Buy real Facebook likes and boost your page instantly today.",
        "Hack any WiFi password with this free app. Download now!",
        "Your IQ is higher than 98% of people. Test confirms this!",
        "You left items in your cart. Complete purchase to get 50% off.",
        "Special invitation for premium members only. Respond today.",
        "This email is only for selected individuals like you. Reply now.",
        "Reminder: Your free trial ends today. Upgrade to keep access.",
        "We have been trying to contact you about your car warranty.",
        "Join thousands earning from our affiliate network. Start today.",
        "Exclusive business opportunity. Only 10 spots left worldwide.",
        "Download this app and earn coins redeemable for real cash.",
        "Your profile was viewed 47 times today. See who viewed you.",
        "Alert: You have unclaimed cashback rewards. Redeem them now.",
        "Get 1TB of cloud storage free for life. Limited time offer only.",
        "NASA scientist reveals trick to boost memory by 300% fast.",
        "Millionaire reveals secret to making money online. Watch now.",
        "This banned video exposes hidden truth. Watch before removed.",
        "Make money by liking posts on social media. No experience needed.",
        "You are invited to an elite investment group. Apply here now.",
        "Breaking: New law gives homeowners $3,000 rebate. Claim yours.",
        "Hurry! Only 3 left in stock. Order now before it sells out.",
        "Your resume has been selected by a top company. Apply today.",
        "We found errors on your credit report. Fix them free today.",
        "A package worth $300 is waiting for you. Pay only $2 shipping.",
        "Receive cash for your opinion. Top surveys pay $50 per hour.",
        "Exclusive webinar reveals how to make $1000 a day online easy.",
        "You have been gifted $10 in credits. Use them before expiry.",
        "Apply now for the easiest job in the world. Earn $200/hour.",
    ]
     
    ham_emails = [
         # ── Casual / Friends / Family ──
        "Just landed in Dubai! Weather is amazing here right now.",
        "Can you recommend a good restaurant near Gulberg? Visiting tonight.",
        "I bought a new laptop finally. Setup took all evening yesterday.",
        "Did you get my voice message? Resending just in case you missed.",
        "Our flight is at 6am. Can you drop me at the airport at 4?",
        "Hope you are settling in well at the new place. Miss you here.",
        "We are planning a road trip to Murree this weekend. Join us!",
        "Finally got a haircut after two months. Feeling much better now.",
        "The mango season is here! Sending some over from our garden.",
        "Long time no talk! How is everything going on your end?",
        "Your birthday gift is on its way. Should arrive by Thursday.",
        "We named the baby Zara. Everyone is healthy and very happy.",
        "Movie night at my place on Friday. Bring popcorn if you can.",
        "I tried that biryani recipe you sent. It turned out amazing!",
        "Just finished a 10km run this morning. New personal best today!",
        "The kids started their summer camp program yesterday. Loving it!",
        "Can you lend me your camera for the wedding this Saturday?",
        "We finally fixed the leaking roof. Took the whole weekend sadly.",
        "Found your old hoodie at mine. Should I drop it off tomorrow?",
        "Karachi weather is unbearable. Stay hydrated and rest inside.",
     
        # ── Work / Professional ──
        "Please review the updated scope of work before tomorrow's call.",
        "The client wants changes to the homepage layout. Details below.",
        "Sprint retrospective notes are attached from yesterday's session.",
        "We onboarded two new developers this week. Introductions Friday.",
        "The marketing campaign goes live on Monday. Assets are ready.",
        "Can you draft the project proposal by end of day Wednesday?",
        "Finance team needs your expense receipts for last month ASAP.",
        "Please update your task status on Jira before the standup.",
        "The vendor has confirmed delivery for Tuesday morning arrival.",
        "Your signature is needed on the NDA before the kickoff call.",
        "New brand guidelines PDF is attached. Please read before Monday.",
        "The intern presentation is at 3pm today in the conference room.",
        "Friendly reminder to complete your mandatory compliance training.",
        "The client escalated an issue. Need a response within 2 hours.",
        "We reached 10,000 monthly active users this week. Great work team!",
        "Please review the revised pricing before the proposal goes out.",
        "Offboarding checklist for Ahmad has been shared with you today.",
        "The team exceeded targets this quarter. Celebration lunch Friday.",
        "Can you join the emergency call in 10 minutes? Link below.",
        "The firewall rules were updated last night. Test your access now.",
     
        # ── Academic / Students / Faculty ──
        "Please review my final year project proposal and give feedback.",
        "The viva schedule has been posted outside the department office.",
        "All students must attend the orientation session on Monday.",
        "The library will conduct a research tools workshop this Thursday.",
        "Plagiarism check is mandatory before final thesis submission.",
        "Department has allocated extra lab hours on Saturday morning.",
        "Your scholarship disbursement is scheduled for next Wednesday.",
        "Please finalize your research topic by this Friday at latest.",
        "The dean has approved the new AI elective for next semester.",
        "Your attendance is below 75%. This may affect your exam eligibility.",
        "Conference abstract submission deadline is October 15th this year.",
        "Peer review assignments for the journal have been sent to you.",
        "The hackathon registration is open. Teams of 3 to 5 members.",
        "Revised grading rubric for assignments has been uploaded today.",
        "Please acknowledge receipt of the internship offer letter below.",
        "Your research grant application has been approved by the board.",
        "All TAs must attend the grading alignment session on Thursday.",
        "The PhD entrance test results will be announced on Friday.",
        "Course withdrawal deadline is this Friday. Act if needed.",
        "The final project demo day is on December 5th in the main hall.",
     
        # ── Notifications / Reminders / Services ──
        "Your electricity meter reading is due by end of this month.",
        "Vehicle token tax is due before April 30. Pay at any branch.",
        "Your CNIC expiry is in 60 days. Renew at the nearest NADRA.",
        "Hospital appointment confirmed: Dr. Sara at 10am on Thursday.",
        "Your monthly bank statement for March is now available online.",
        "Gas connection restoration scheduled for Friday between 10 and 12.",
        "Reminder: annual eye checkup is overdue. Book an appointment.",
        "Your child's school fee is due by the 10th of this month.",
        "The property tax notice has been mailed to your registered address.",
        "Your passport renewal application is under processing currently.",
        "Flight PK301 is on time. Boarding starts at gate 7 at 5:40am.",
        "Your SIM verification is pending. Visit any franchise within 7 days.",
        "New e-statement for your credit card is ready to download now.",
        "Your health insurance card has been dispatched via courier today.",
        "Biometric verification required at branch before account activation.",
     
        # ── Tech / Developer / IT ──
        "I opened a GitHub issue for the bug we discussed. Link below.",
        "The staging server SSL certificate expires in 7 days. Renew it.",
        "Can you review the database schema changes before I migrate?",
        "The WebSocket connection keeps dropping under high load today.",
        "Memory leak found in the background task. Fix pushed to dev.",
        "Could you add error logging to the payment service endpoint?",
        "The cron job ran at wrong time due to timezone mismatch in config.",
        "We need to write integration tests for the new auth flow soon.",
        "Postman collection for the new API endpoints has been shared.",
        "The deployment to production failed. Rollback initiated automatically.",
        "FastAPI response time increased after the latest merge. Investigating.",
        "Can you set up a Redis queue for the email sending service?",
        "The client wants a dark mode option. Can we estimate the effort?",
        "Rate limiter is blocking some valid requests. Needs tuning soon.",
        "AWS costs spiked this month. CloudWatch logs attached for review.",
        "GraphQL schema has been updated. Regenerate your local types.",
        "The mobile app crashes on Android 13. Steps to reproduce below.",
        "Celery worker is not picking up tasks after the server restart.",
        "Please document the new endpoints in the shared Notion page.",
        "Environment variables updated on staging. Re-deploy your branch.",
     
        # ── Health / Wellness ──
        "Doctor said results are normal. Nothing to worry about, alhamdulillah.",
        "Started my physiotherapy sessions this week. Feeling some relief.",
        "Please remind everyone to stay hydrated during these hot days.",
        "Health camp is being organized on campus next Saturday morning.",
        "Mental health awareness session tomorrow. All staff encouraged.",
        "The blood drive is on Thursday. Eligible donors please register.",
        "My nutritionist suggested reducing sugar. Sharing the plan below.",
        "Please take your medication on time. I left it on the kitchen table.",
        "Yoga classes start Monday at 7am in the community center hall.",
        "I recovered fully. Thank you for checking in and your prayers.",
        # Casual / Personal
        "Hey, can we meet tomorrow for coffee at the usual place?",
        "Let me know when you are free for a quick call.",
        "Happy birthday! Hope you have a wonderful day today.",
        "Mom called. She wants you to come home this weekend.",
        "Ali sent you a friend request on the platform.",
        "Ramadan Mubarak to you and your entire family!",
        "I am heading out now. Will be there in about 20 minutes.",
        "Just checking in. How have you been doing lately?",
        "Are you joining us for dinner tonight? Let me know soon.",
        "I got the parcel you sent. Thank you so much for it!",
        "Safe travels! Let me know when you land safely please.",
        "Did you watch the match last night? What a game it was!",
        "How did your interview go today? Hope it went well.",
        "I am feeling a bit under the weather. Won't make it today.",
        "Your photos from the trip are amazing. Share them please!",
        "Congratulations on your promotion! You deserve it completely.",
        "We are having a small gathering Saturday. Hope you can come.",
        "Can you pick up some groceries on your way home please?",
        "The kids are asking about you. Come visit us soon please.",
        "I finally finished reading that book you recommended. Loved it!",
        "Eid Mubarak! Wishing you and family a joyful celebration.",
        "Just saw your LinkedIn update. Big congratulations to you!",
        "Are you free this weekend? Let us plan something fun together.",
        "Send me your new address. I want to send you something nice.",
        "Thanks for the birthday wishes. Really made my day special.",
     
        # Work / Office
        "The project report is due on Friday. Please review it.",
        "The server is down. Please check and let me know.",
        "Please find attached the invoice for last month services.",
        "The code review is done. A few minor changes needed.",
        "Team lunch is at 1pm today at the usual restaurant.",
        "I reviewed your proposal. It looks good, minor edits needed.",
        "Can you forward me the client contact details please?",
        "I will be working from home next week. Available on Slack.",
        "I have attached the corrected version of the report.",
        "Please join the group call at 4pm using the link below.",
        "The parking area will be closed tomorrow for maintenance.",
        "Network maintenance tonight from 11pm to 2am. Save your work.",
        "The project deadline has been extended to next Friday.",
        "Your application has been received. We will contact you soon.",
        "Please confirm your attendance for the seminar by Thursday.",
        "The meeting notes are attached. Please review before Friday.",
        "Can you send me the budget breakdown for this quarter?",
        "We need to finalize the contract by end of day tomorrow.",
        "The client approved the design. We can proceed to development.",
        "HR is requesting updated emergency contact details from all staff.",
        "Please submit your timesheet by 5pm this Friday without fail.",
        "The new company policy document is attached for your review.",
        "Your leave request has been approved by the department head.",
        "The quarterly targets have been shared on the internal portal.",
        "Can we move the standup to 10am tomorrow instead of 9am?",
        "The sales figures for March are now available on the dashboard.",
        "Please review the attached draft before the client meeting.",
        "All staff are required to attend the fire drill on Wednesday.",
        "The office will be closed on Thursday for a public holiday.",
        "Your performance review is scheduled for next Tuesday morning.",
        "The new project management tool goes live from Monday onward.",
        "I will be on annual leave from Monday to Thursday this week.",
        "Could you handle the client call on my behalf tomorrow please?",
        "The board meeting slides need to be ready by Sunday evening.",
        "A new vendor onboarding form has been sent to your email.",
        "Please coordinate with the logistics team for the delivery.",
        "The IT team needs your laptop for an update this afternoon.",
        "Security badges will be reissued to all employees next week.",
        "Feedback from last week's workshop has been compiled and shared.",
        "Please ensure all devices are backed up before the upgrade.",
     
        # Academic / University
        "Can you send me the lecture notes from today please?",
        "Great work on the NLP presentation. Students loved it.",
        "I finished the assignment last night. Will submit tomorrow.",
        "The class starts at 9am tomorrow. Please be on time.",
        "Can we reschedule our meeting to next Monday morning?",
        "The library book you requested is now available for pickup.",
        "Can you help me debug this Python code after class?",
        "I passed my NLP exam! Thank you for the study help.",
        "The exam results are out. Check the student portal now.",
        "Please bring your student ID card to the exam hall.",
        "The cafeteria menu has been updated. New items added.",
        "Training session at 2pm in room 301. Please attend.",
        "The lab computers will be updated this weekend. Plan accordingly.",
        "Could you review my thesis chapter before I submit it?",
        "Thank you for your help with the Python assignment yesterday.",
        "I enjoyed your lecture on deep learning today. Very clear!",
        "The new semester schedule is now available on the portal.",
        "Looking forward to seeing you at the conference next week.",
        "Please submit your assignment before midnight tonight.",
        "The wifi password has changed. New password is shared below.",
        "Quiz tomorrow covers chapters 4 through 7. Please prepare.",
        "The seminar registration link has been sent to your inbox.",
        "Faculty meeting rescheduled to Thursday at 11am in Hall B.",
        "Research paper submission deadline is extended by one week.",
        "The department is offering a free machine learning workshop.",
        "Your scholarship application has moved to the next round.",
        "A guest lecture on AI ethics is scheduled for next Monday.",
        "Lab session moved from Room 201 to Room 305 this Friday.",
        "Please upload your project files to the shared drive today.",
        "The exam timetable has been posted on the department board.",
        "All students must complete course evaluation by this Friday.",
        "The internship fair is next Wednesday. Bring printed CVs.",
        "Extra credit opportunity: attend the research symposium tomorrow.",
        "Your thesis supervisor has left comments on your draft today.",
        "The university library will be closed on Friday for renovation.",
        "Please register for next semester courses before December 15.",
        "I will hold extra office hours on Wednesday from 2 to 4pm.",
        "The assignment rubric has been updated. Please check it again.",
        "Group project presentations are on Thursday. 10 minutes each.",
        "All final year students must submit clearance forms this week.",
     
        # Appointments / Notifications
        "Your appointment is confirmed for Thursday at 3pm.",
        "The electricity bill is due tomorrow. Please pay online.",
        "Your package has been delivered to the front desk.",
        "Your subscription renews on March 1st. Check your settings.",
        "Bus timings have changed. Please check the updated schedule.",
        "The electricity will be off from 10am to 12pm tomorrow.",
        "Your car service is due next week. Book your appointment.",
        "Your prescription is ready for pickup at the pharmacy.",
        "Reminder: dental appointment tomorrow at 11am. Please confirm.",
        "The plumber is scheduled to arrive between 9am and 11am.",
        "Your visa application status has been updated. Check online.",
        "Your internet plan renewal is due in 5 days. Renew early.",
        "The gym will be closed this Sunday for scheduled maintenance.",
        "Your test results are ready. Please visit the clinic to collect.",
        "Reminder: your driving license expires in 30 days. Renew now.",
        "Your online order has been shipped. Expected delivery is Friday.",
        "Appointment rescheduled to Monday at 2pm. Please confirm.",
        "Your blood donation appointment is confirmed for Saturday.",
        "The community meeting is on Tuesday at 7pm in the main hall.",
        "Parking permit renewal is due by the end of this month.",
        "Your insurance policy renewal reminder is attached for review.",
        "Water supply will be interrupted on Thursday from 8am to 2pm.",
        "Your feedback form for the recent service has been sent below.",
        "The vaccination camp is on Saturday from 9am to 3pm. Register.",
        "Road work ahead: alternate routes suggested for this weekend.",
     
        # Tech / Developer
        "The server is down. Please check and let me know.",
        "Can you help me debug this Python code after class?",
        "The code review is done. A few minor changes needed.",
        "I have pushed the changes to the main branch. Please review.",
        "The API is returning a 500 error. Can you check the logs?",
        "New version deployed to staging. Please run your tests now.",
        "The Docker container keeps crashing. I checked and logs attached.",
        "Can you approve my pull request when you get a chance?",
        "Unit tests are failing after the latest merge. Investigating now.",
        "The database migration ran successfully on the dev environment.",
        "CI pipeline is broken. Looks like a dependency version conflict.",
        "We need to refactor the authentication module before release.",
        "The front end build is failing. Webpack config issue probably.",
        "Redis cache is hitting max memory. We need to adjust the config.",
        "Scheduled job ran 3 hours late last night. Investigating cause.",
        "Feature branch ready for testing. Link to staging environment below.",
        "Could you write unit tests for the payment module by Friday?",
        "The load balancer config was updated. Keep an eye on latency.",
        "SQL query is running slow. Added index but still needs review.",
        "We need to upgrade the Python version from 3.9 to 3.12 soon.",
    ]

    texts  = spam_emails + ham_emails
    labels = ['spam'] * len(spam_emails) + ['ham'] * len(ham_emails)
    df = pd.DataFrame({'text': texts, 'label': labels})
    print(f"  Demo dataset created: {len(df)} emails")

# ── Basic info ────────────────────────────────────────────
print(f"\n  Shape: {df.shape}")
print(f"\n  First 5 rows:")
print(df.head())

print(f"\n  Class Distribution:")
dist = df['label'].value_counts()
for label, count in dist.items():
    pct = count / len(df) * 100
    bar = "█" * int(pct / 2)
    print(f"    {label:>6}: {count:>4} ({pct:.1f}%)  {bar}")


# ============================================================
# STEP 2: EXPLORATORY DATA ANALYSIS (EDA)
# ============================================================

print("\n" + "=" * 60)
print("STEP 2: EXPLORATORY DATA ANALYSIS")
print("=" * 60)

# ── Text length analysis ──────────────────────────────────
df['text_length'] = df['text'].apply(len)
df['word_count']  = df['text'].apply(lambda x: len(x.split()))

print("\n  Text Length Stats by Class:")
print(df.groupby('label')[['text_length', 'word_count']].describe().round(1))

# ── Encode labels ─────────────────────────────────────────
df['label_num'] = df['label'].map({'spam': 1, 'ham': 0})

# ── Plot distributions ────────────────────────────────────
fig, axes = plt.subplots(1, 3, figsize=(15, 4))
fig.suptitle('Spam Detector — EDA', fontsize=14, fontweight='bold')

# Class distribution
dist.plot(kind='bar', ax=axes[0], color=['#2ecc71', '#e74c3c'], edgecolor='black')
axes[0].set_title('Class Distribution')
axes[0].set_xlabel('Label')
axes[0].set_ylabel('Count')
axes[0].tick_params(axis='x', rotation=0)

# Text length by class
df[df['label'] == 'ham']['text_length'].hist(
    ax=axes[1], alpha=0.7, color='#2ecc71', label='Ham', bins=20)
df[df['label'] == 'spam']['text_length'].hist(
    ax=axes[1], alpha=0.7, color='#e74c3c', label='Spam', bins=20)
axes[1].set_title('Text Length Distribution')
axes[1].set_xlabel('Characters')
axes[1].legend()

# Word count by class
df[df['label'] == 'ham']['word_count'].hist(
    ax=axes[2], alpha=0.7, color='#2ecc71', label='Ham', bins=20)
df[df['label'] == 'spam']['word_count'].hist(
    ax=axes[2], alpha=0.7, color='#e74c3c', label='Spam', bins=20)
axes[2].set_title('Word Count Distribution')
axes[2].set_xlabel('Words')
axes[2].legend()

plt.tight_layout()
plt.savefig('eda_analysis.png', dpi=150, bbox_inches='tight')
# plt.show()
print("  EDA plot saved as: eda_analysis.png")


# ============================================================
# STEP 3: TEXT PRE-PROCESSING (full NLP pipeline)
# ============================================================

print("\n" + "=" * 60)
print("STEP 3: NLP PRE-PROCESSING PIPELINE")
print("=" * 60)

stop_words  = set(stopwords.words('english'))
lemmatizer  = WordNetLemmatizer()

def preprocess(text):
    """
    Full NLP pre-processing pipeline:
    1. Lowercase
    2. Remove URLs
    3. Remove punctuation and numbers
    4. Tokenize
    5. Remove stopwords
    6. Lemmatize
    """
    # Step 1: Lowercase
    text = text.lower()

    # Step 2: Remove URLs
    text = re.sub(r'http\S+|www\S+', '', text)

    # Step 3: Remove punctuation and numbers
    text = re.sub(r'[^a-z\s]', '', text)

    # Step 4: Remove extra whitespace
    text = re.sub(r'\s+', ' ', text).strip()

    # Step 5: Tokenize
    tokens = word_tokenize(text)

    # Step 6: Remove stopwords
    tokens = [t for t in tokens if t not in stop_words and len(t) > 1]

    # Step 7: Lemmatize
    tokens = [lemmatizer.lemmatize(t) for t in tokens]

    return " ".join(tokens)

# ── Show pipeline in action ───────────────────────────────
print("\n  Pipeline demo on 3 examples:")
sample_indices = [0, len(df)//2, -1]
for i in sample_indices:
    original = df['text'].iloc[i]
    cleaned  = preprocess(original)
    label    = df['label'].iloc[i]
    print(f"\n  [{label.upper()}]")
    print(f"    Before: '{original[:80]}...'")
    print(f"    After : '{cleaned[:80]}...'")

# ── Apply to full dataset ─────────────────────────────────
print("\n  Processing all emails...")
df['clean_text'] = df['text'].apply(preprocess)
print(f"  Done! {len(df)} emails processed.")

# ── Vocabulary size before/after ─────────────────────────
vocab_before = set(" ".join(df['text']).lower().split())
vocab_after  = set(" ".join(df['clean_text']).split())
print(f"\n  Vocabulary BEFORE cleaning: {len(vocab_before):,} words")
print(f"  Vocabulary AFTER  cleaning: {len(vocab_after):,} words")
print(f"  Reduction: {len(vocab_before) - len(vocab_after):,} words removed")


# ============================================================
# STEP 4: VECTORIZATION (TF-IDF)
# ============================================================

print("\n" + "=" * 60)
print("STEP 4: TF-IDF VECTORIZATION")
print("=" * 60)

tfidf = TfidfVectorizer(
    max_features = 3000,     # keep top 3000 words
    ngram_range  = (1, 2),   # use single words AND word pairs
    min_df       = 2,        # word must appear in at least 2 docs
    max_df       = 0.95,     # ignore words in more than 95% of docs
)

X = tfidf.fit_transform(df['clean_text'])
y = df['label_num'].values

print(f"\n  TF-IDF Matrix shape: {X.shape}")
print(f"  Rows    = {X.shape[0]} emails")
print(f"  Columns = {X.shape[1]} features (words/phrases)")

# ── Top spam vs ham words ─────────────────────────────────
print("\n  Top 10 words in SPAM emails:")
spam_docs = df[df['label'] == 'spam']['clean_text']
ham_docs  = df[df['label'] == 'ham']['clean_text']

spam_tfidf = TfidfVectorizer(max_features=10).fit(spam_docs)
ham_tfidf  = TfidfVectorizer(max_features=10).fit(ham_docs)

print(f"    {list(spam_tfidf.vocabulary_.keys())}")
print(f"\n  Top 10 words in HAM emails:")
print(f"    {list(ham_tfidf.vocabulary_.keys())}")

# ============================================================
# STEP 5: FEATURE SELECTION
# ============================================================

print("\n" + "=" * 60)
print("STEP 5: FEATURE SELECTION (Chi-Square)")
print("=" * 60)

k_features = min(1500, X.shape[1])
selector   = SelectKBest(chi2, k=k_features)
X_selected = selector.fit_transform(X, y)

print(f"\n  Features before selection: {X.shape[1]}")
print(f"  Features after  selection: {X_selected.shape[0]}")
print(f"  Removed {X.shape[1] - X_selected.shape[0]} low-importance features")

# ── Top most discriminative features ─────────────────────
feature_names = tfidf.get_feature_names_out()
selected_mask = selector.get_support()
chi2_scores   = selector.scores_

top_features = sorted(zip(feature_names, chi2_scores),key=lambda x: x[1], reverse=True)[:15]

print(f"\n  Top 15 most discriminative features:")
print(f"  {'Feature':<25} {'Chi2 Score':>12}  Bar")
print(f"  {'-'*55}")
max_score = top_features[0][1]
for feat, score in top_features:
    bar = "█" * int(score / max_score * 25)
    print(f"  {feat:<25} {score:>12.2f}  {bar}")



# ============================================================
# STEP 6: HANDLE CLASS IMBALANCE WITH SMOTE
# ============================================================

print("\n" + "=" * 60)
print("STEP 6: HANDLE IMBALANCE WITH SMOTE")
print("=" * 60)

from collections import Counter

print(f"\n  Before SMOTE: {Counter(y)}")

# Convert sparse matrix to array for SMOTE
X_dense = X_selected.toarray()

smote = SMOTE(random_state=42)
# print(smote)

X_balanced, y_balanced = smote.fit_resample(X_dense, y)
# print(X_balanced)
# print(y_balanced)
print(f"  After  SMOTE: {Counter(y_balanced)}")
print(f"  Added {Counter(y_balanced)[1] - Counter(y)[1]} synthetic spam samples")


# ============================================================
# STEP 7: TRAIN / TEST SPLIT
# ============================================================

print("\n" + "=" * 60)
print("STEP 7: TRAIN / TEST SPLIT")
print("=" * 60)

X_train, X_test, y_train, y_test = train_test_split(
    X_balanced, y_balanced,
    test_size    = 0.2,
    random_state = 42,
    stratify     = y_balanced
)

print(f"\n  Total samples : {len(X_balanced)}")
print(f"  Training set  : {len(X_train)} ({len(X_train)/len(X_balanced)*100:.0f}%)")
print(f"  Test set      : {len(X_test)} ({len(X_test)/len(X_balanced)*100:.0f}%)")
print(f"  Features      : {X_train.shape[1]}")


# ============================================================
# STEP 8: TRAIN THREE MODELS AND COMPARE
# ============================================================

print("\n" + "=" * 60)
print("STEP 8: TRAIN AND COMPARE MODELS")
print("=" * 60)

models = {
    "Naive Bayes"        : MultinomialNB(alpha=0.1),
    "Logistic Regression": LogisticRegression(max_iter=1000, random_state=42),
    "Linear SVM"         : LinearSVC(random_state=42, max_iter=2000),
}

results = {}

for name, model in models.items():
    print(f"\n  Training {name}...")
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)

    acc  = accuracy_score(y_test, y_pred)
    prec = precision_score(y_test, y_pred)
    rec  = recall_score(y_test, y_pred)
    f1   = f1_score(y_test, y_pred)

    # AUC only for models with predict_proba
    try:
        y_prob = model.predict_proba(X_test)[:, 1]
        auc    = roc_auc_score(y_test, y_prob)
    except AttributeError:
        y_prob = None
        auc    = 0.0

    results[name] = {
        'model'    : model,
        'y_pred'   : y_pred,
        'y_prob'   : y_prob,
        'accuracy' : acc,
        'precision': prec,
        'recall'   : rec,
        'f1'       : f1,
        'auc'      : auc,
    }

    print(f"    Accuracy  : {acc:.4f}")
    print(f"    Precision : {prec:.4f}")
    print(f"    Recall    : {rec:.4f}")
    print(f"    F1-Score  : {f1:.4f}")
    print(f"    AUC-ROC   : {auc:.4f}")


# ============================================================
# STEP 9: DETAILED EVALUATION — BEST MODEL
# ============================================================

print("\n" + "=" * 60)
print("STEP 9: DETAILED EVALUATION")
print("=" * 60)

# Pick best model by F1-Score
best_name = max(results, key=lambda k: results[k]['f1'])
best      = results[best_name]

print(f"\n  Best model: {best_name} (F1 = {best['f1']:.4f})")
print(f"\n  Classification Report:")
print(classification_report(y_test, best['y_pred'],
                            target_names=['Ham', 'Spam']))

# ── Confusion Matrix ──────────────────────────────────────
cm = confusion_matrix(y_test, best['y_pred'])

fig, axes = plt.subplots(1, 3, figsize=(18, 5))
fig.suptitle(f'Model Evaluation — {best_name}', fontsize=14, fontweight='bold')

# Confusion matrix heatmap
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues',
            xticklabels=['Ham', 'Spam'],
            yticklabels=['Ham', 'Spam'],
            ax=axes[0], linewidths=0.5)
axes[0].set_title('Confusion Matrix')
axes[0].set_xlabel('Predicted')
axes[0].set_ylabel('Actual')

# Model comparison bar chart
metric_names = ['Accuracy', 'Precision', 'Recall', 'F1-Score']
x = np.arange(len(metric_names))
width = 0.25
colors = ['#3498db', '#2ecc71', '#e74c3c']
for i, (name, res) in enumerate(results.items()):
    vals = [res['accuracy'], res['precision'], res['recall'], res['f1']]
    axes[1].bar(x + i * width, vals, width, label=name,
                color=colors[i], alpha=0.85, edgecolor='black')
axes[1].set_title('Model Comparison')
axes[1].set_xticks(x + width)
axes[1].set_xticklabels(metric_names)
axes[1].set_ylim(0, 1.1)
axes[1].legend(fontsize=8)
axes[1].set_ylabel('Score')

# ROC Curve (models with probability)
axes[2].plot([0, 1], [0, 1], 'k--', label='Random (AUC=0.5)')
for i, (name, res) in enumerate(results.items()):
    if res['y_prob'] is not None:
        fpr, tpr, _ = roc_curve(y_test, res['y_prob'])
        axes[2].plot(fpr, tpr, color=colors[i],
                     label=f"{name} (AUC={res['auc']:.3f})")
axes[2].set_title('ROC Curve')
axes[2].set_xlabel('False Positive Rate')
axes[2].set_ylabel('True Positive Rate')
axes[2].legend(fontsize=8)

plt.tight_layout()
plt.savefig('model_evaluation.png', dpi=150, bbox_inches='tight')
# plt.show()
print("  Evaluation plot saved as: model_evaluation.png")

# ── Confusion matrix explained ────────────────────────────
tn, fp, fn, tp = cm.ravel()
print(f"\n  Confusion Matrix Breakdown:")
print(f"    TP (Spam caught correctly)     : {tp}")
print(f"    TN (Ham passed correctly)      : {tn}")
print(f"    FP (Ham wrongly flagged spam)  : {fp}  ← false alarm")
print(f"    FN (Spam that slipped through) : {fn}  ← dangerous miss")


# ============================================================
# STEP 10: TEST ON NEW EMAILS
# ============================================================

print("\n" + "=" * 60)
print("STEP 10: TEST ON NEW EMAILS")
print("=" * 60)

best_model = best['model']

new_emails = [
    "Congratulations! You won a free iPhone. Click here now!",
    "Hey, can we meet tomorrow for coffee?",
    "URGENT: Your account is suspended. Verify immediately!",
    "Please submit your assignment before midnight.",
    "Win $1000 cash prize. Text WIN to 87121 now.",
    "The class is cancelled tomorrow. Stay home.",
    "Buy cheap medicine online. No prescription needed.",
    "I enjoyed your NLP lecture today. Very helpful!",
    "You are selected as a lucky winner. Claim your prize!",
    "Can you review my Python code when you have time?",
]

print(f"\n  {'#':<3} {'Result':<12} {'Confidence':>12}  Email preview")
print(f"  {'-'*75}")

for i, email in enumerate(new_emails):
    cleaned    = preprocess(email)
    vectorized = tfidf.transform([cleaned])
    selected   = selector.transform(vectorized).toarray()
    prediction = best_model.predict(selected)[0]

    # Confidence score
    try:
        prob       = best_model.predict_proba(selected)[0]
        confidence = prob[prediction]
        conf_str   = f"{confidence:.0%}"
    except AttributeError:
        conf_str   = "N/A"

    label    = "🔴 SPAM" if prediction == 1 else "🟢 HAM"
    preview  = email[:45] + "..." if len(email) > 45 else email
    print(f"  {i+1:<3} {label:<12} {conf_str:>12}  '{preview}'")


# ============================================================
# STEP 11: FULL PIPELINE RECAP
# ============================================================

print("\n" + "=" * 60)
print("PIPELINE RECAP — What We Built")
print("=" * 60)
print("""
  Step 1:  Load Data         → pandas read_csv (spam.csv)
  Step 2:  EDA               → class distribution, text length
  Step 3:  Pre-processing    → lowercase, remove URLs/punct,
                               tokenize, remove stopwords, lemmatize
  Step 4:  TF-IDF            → convert clean text to numbers
  Step 5:  Feature Selection → Chi-Square, keep top 1500 features
  Step 6:  SMOTE             → fix class imbalance synthetically
  Step 7:  Train/Test Split  → 80% train, 20% test
  Step 8:  Train 3 Models    → Naive Bayes, Logistic Reg, SVM
  Step 9:  Evaluate          → Accuracy, Precision, Recall, F1, AUC
  Step 10: Predict           → test on brand new emails

  Metrics used:
  ├── Accuracy   → overall correctness
  ├── Precision  → how many flagged spam were actually spam
  ├── Recall     → how many real spam emails were caught
  ├── F1-Score   → balance of precision and recall
  └── AUC-ROC    → model quality across all thresholds

  Every step maps directly to lecture content.
""")