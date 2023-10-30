import streamlit as st
import re
from streamlit_chat import message
from bardapi import Bard
import os

os.environ["_BARD_API_KEY"] = "bwjaaBBIgjdLsrWCMYCvSyOvCQaKI3GFOhqw5G3_QXRgw37ZrI0MGKP0n7riLkA-31teOg."

class ChatBot:
    def message_probability(self, user_message, recognised_words, single_response=False, required_words=[]):
        message_certainty = 0
        has_required_words = True

        for word in user_message:
            if word in recognised_words:
                message_certainty += 1

        percentage = float(message_certainty) / float(len(recognised_words))

        for word in required_words:
            if word not in user_message:
                has_required_words = False
                break

        if has_required_words or single_response:
            return int(percentage * 100)
        else:
            return 0

    def check_all_messages(self, message):
        highest_prob_list = {}

        def response(bot_response, list_of_words, single_response=False, required_words=[]):
            nonlocal highest_prob_list
            highest_prob_list[bot_response] = self.message_probability(message, list_of_words, single_response, required_words)

        response('Hello!', ['hello', 'hi', 'hey', 'sup', 'heyo'], single_response=True)
        response('See you!', ['bye', 'goodbye'], single_response=True)
        response('I\'m doing fine, and you?', ['how', 'are', 'you', 'doing'], required_words=['how'])
        response('You\'re welcome!', ['thank', 'thanks'], single_response=True)
        response('Thank you!', ['i', 'love', 'code', 'palace'], required_words=['code', 'palace'])
        response('How may I help you?', ['i', 'need', 'help'], required_words=['help'])
        response('My apologies! Could you repeat it?', ['cant', 'you', 'understand'], required_words=['understand', 'cant'])
        response('Mental illnesses are health conditions that disrupt a person\'s thoughts, emotions, relationships, and daily functioning.', ['mental', 'what', 'illness'], required_words=['what', 'mental'])
        response('suicide is never an option.Talk to your loved ones',['i','want','to','die','suicide','end','it'],required_words=['i','want','suicide'])
        response('i was created to assist patients',['why','were','you','created'],required_words=['why','created'])
        response('i am today years old!',['how','old','are','you?'],required_words=['how','old','you'])
        response('Please further elaborate your condition',['i', 'am','feeling','sick'],required_words=['i','feeling','sick'])
        response('paracetamol is an tablet taken for fever',['what','is','paracetamol','to','take','for','fever','medicine'],required_words=['fever','medicine'])
        response('It is recommended to take rest and take steam',['i','have','cold','what','to','do'],required_words=['cold'])
        response("Eating a balanced diet, staying physically active, and managing stress are essential for maintaining a healthy weight. Would you like more tips on how to maintain a healthy weight?", ['how', 'can', 'I', 'maintain', 'a', 'healthy', 'weight'], required_words=['how', 'maintain', 'healthy', 'weight'])

        response("Regular physical activity has numerous benefits, including improved cardiovascular health, weight management, and reduced stress. Would you like to know more about the advantages of regular physical activity?", ['what', 'are', 'the', 'benefits', 'of', 'regular', 'physical', 'activity'], required_words=['benefits', 'of', 'regular', 'physical', 'activity'])

        response("The recommended daily water intake varies but is generally around 8-10 glasses (about 2-2.5 liters) of water per day for adults. Staying hydrated is important for overall well-being. Would you like more information on the importance of hydration?", ['how', 'much', 'water', 'should', 'I', 'drink', 'daily', 'for', 'good', 'health'], required_words=['how', 'much', 'water', 'should', 'drink'])

        response("Adequate sleep is crucial for physical and mental well-being. It's generally recommended for adults to get 7-9 hours of sleep per night. Would you like to learn more about the importance of sleep?", ['what', 'is', 'the', 'importance', 'of', 'sleep', 'for', 'good', 'health'], required_words=['importance', 'of', 'sleep'])

        response("Reducing stress in daily life is essential for well-being. There are various stress reduction techniques, including mindfulness, exercise, and relaxation. Would you like more information on how to reduce stress?", ['how', 'can', 'I', 'reduce', 'stress', 'in', 'my', 'daily', 'life'], required_words=['how', 'reduce', 'stress'])

        response("Oral hygiene is vital for maintaining good dental health. Best practices include brushing and flossing regularly, visiting your dentist, and maintaining a healthy diet. Would you like more dental care tips?", ['what', 'are', 'the', 'best', 'practices', 'for', 'oral', 'hygiene'], required_words=['best', 'practices', 'for', 'oral', 'hygiene'])

        response("Preventing common illnesses like colds and the flu involves good hygiene practices and vaccinations. Would you like more tips on how to prevent common illnesses?", ['how', 'can', 'I', 'prevent', 'common', 'illnesses', 'like', 'colds', 'and', 'the', 'flu'], required_words=['how', 'prevent', 'common', 'illnesses', 'like', 'colds', 'and', 'the', 'flu'])

        response("Regular exercise has numerous benefits, including weight management, improved mood, and enhanced cardiovascular health. Would you like to know more about the advantages of regular physical activity?", ['what', 'are', 'the', 'advantages', 'of', 'regular', 'physical', 'activity'], required_words=['advantages', 'of', 'regular', 'physical', 'activity'])

        response("Improving mental health and emotional well-being can be achieved through various methods such as therapy, stress management, and self-care. Would you like more tips on how to promote better mental health?", ['how', 'can', 'I', 'improve', 'my', 'mental', 'health', 'and', 'emotional', 'well-being'], required_words=['how', 'improve', 'my', 'mental', 'health', 'and', 'emotional', 'well-being'])

        response("A balanced diet plays a crucial role in maintaining overall well-being. Would you like to learn more about the role of a balanced diet in health?", ['what', 'is', 'the', 'role', 'of', 'a', 'balanced', 'diet', 'in', 'maintaining', 'overall', 'well-being'], required_words=['role', 'of', 'a', 'balanced', 'diet', 'in', 'maintaining', 'overall', 'well-being'])

        response("Maintaining good heart health involves a healthy diet, regular exercise, and avoiding smoking. Would you like more information on maintaining good heart health?", ['how', 'can', 'I', 'maintain', 'good', 'heart', 'health', 'throughout', 'my', 'life'], required_words=['how', 'maintain', 'good', 'heart', 'health'])

        response("Regular check-ups with a healthcare provider have benefits like early disease detection. Would you like to know more about the advantages of regular check-ups?", ['what', 'are', 'the', 'benefits', 'of', 'regular', 'check-ups', 'with', 'a', 'healthcare', 'provider'], required_words=['benefits', 'of', 'regular', 'check-ups'])
        response('There are plentiful ways to gain weight:Eat periodically,try to gain muscle mass by weight lifting,be in calorie surplus',['how','to','gain','weight'],required_words=['weight','gain'])
        response("For a cold, you can also try using a humidifier, drinking hot soup, and getting plenty of rest. If your symptoms persist or worsen, it's advisable to consult a healthcare professional.", ['cold', 'home', 'remedies'], required_words=['cold', 'home', 'remedies'])
        response("I'm here to provide support and information to patients. If you have any health-related questions or concerns, feel free to ask.", ['what', 'is', 'your', 'purpose', 'created'], required_words=['purpose', 'created'])
        response("Vaccinations are crucial to prevent various diseases and boost immunity. Consult your healthcare provider for recommended vaccinations.", ['why', 'are', 'vaccinations', 'important'], required_words=['vaccinations'])
        response("Pregnancy is a complex process that typically lasts about 40 weeks, with various stages and prenatal care required for a healthy pregnancy.", ['what', 'happens', 'during', 'pregnancy'], required_words=['pregnancy'])
        response("Allergies occur when the immune system reacts to a foreign substance, triggering symptoms like sneezing, itching, and rashes.", ['what', 'are', 'allergies'], required_words=['allergies'])
        response("Cholesterol is a fatty substance in your blood. High levels can increase the risk of heart disease.", ['what', 'is', 'cholesterol'], required_words=['cholesterol'])
        response("For mental health support, consider talking to a mental health professional, engaging in therapy, or seeking community resources.", ['how', 'to', 'get', 'mental', 'health', 'support'], required_words=['mental', 'health', 'support'])
        response("Stress management techniques include deep breathing, relaxation exercises, and time management to reduce stress levels.", ['how', 'to', 'manage', 'stress'], required_words=['manage', 'stress'])
        response("Anxiety is a common mental health condition. Treatment may involve therapy, medication, or self-help strategies.", ['what', 'is', 'anxiety'], required_words=['anxiety'])
        response("Self-care for mental health involves practicing self-compassion, setting boundaries, and seeking support from loved ones.", ['how', 'to', 'practice', 'self-care', 'for', 'mental', 'health'], required_words=['self-care', 'mental', 'health'])
        response("PTSD can develop after a traumatic event. Treatment may include therapy, medication, and support groups.", ['what', 'is', 'PTSD'], required_words=['PTSD'])
        response("Reducing the stigma around mental health is essential for promoting understanding and seeking help without fear of judgment.", ['how', 'to', 'reduce', 'mental', 'health', 'stigma'], required_words=['reduce', 'mental', 'health', 'stigma'])
        response("ADHD is a neurodevelopmental disorder that can affect focus and impulse control. Treatment may include therapy and medication.", ['what', 'is', 'ADHD'], required_words=['ADHD'])
        response("Schizophrenia is a complex mental disorder with symptoms like hallucinations and delusions. It typically requires lifelong treatment.", ['what', 'is', 'schizophrenia'], required_words=['schizophrenia'])
        response("If you or someone you know is struggling with mental health, consider reaching out to a mental health professional for evaluation and support.", ['how', 'to', 'seek', 'help', 'for', 'mental', 'health'], required_words=['seek', 'help', 'mental', 'health'])
        response("Coping with stress involves various techniques, such as mindfulness meditation, exercise, and spending time in nature.", ['how', 'to', 'cope', 'with', 'stress'], required_words=['cope', 'stress'])
        response("Panic attacks can be overwhelming but are manageable. Breathing exercises and grounding techniques can help during an attack.", ['what', 'to', 'do', 'during', 'a', 'panic', 'attack'], required_words=['panic', 'attack'])
        response("Social anxiety is characterized by a fear of social situations. Cognitive-behavioral therapy can be effective in treating it.", ['how', 'to', 'deal', 'with', 'social', 'anxiety'], required_words=['deal', 'social', 'anxiety'])
        response("Building self-esteem involves self-acceptance, positive self-talk, and setting achievable goals for personal growth.", ['how', 'to', 'improve', 'self-esteem'], required_words=['improve', 'self-esteem'])
        response("Eating disorders like anorexia and bulimia require professional treatment and support. Early intervention is crucial.", ['what', 'are', 'eating', 'disorders'], required_words=['eating', 'disorders'])
        response("Mindfulness meditation is a practice that helps reduce stress and improve mental well-being. It involves being fully present in the moment.", ['what', 'is', 'mindfulness', 'meditation'], required_words=['mindfulness', 'meditation'])
        response("Treatment options for PTSD include cognitive-behavioral therapy (CBT), eye movement desensitization and reprocessing (EMDR), and medication.", ['how', 'is', 'PTSD', 'treated'], required_words=['PTSD', 'treated'])
        response("Supporting loved ones with mental health issues involves active listening, empathy, and encouraging them to seek professional help.", ['how', 'to', 'support', 'someone', 'with', 'mental', 'health', 'issues'], required_words=['support', 'mental', 'health', 'issues'])
        response("Generalized Anxiety Disorder (GAD) involves excessive worry and anxiety about everyday events. Cognitive-behavioral therapy is an effective treatment.", ['how', 'to', 'manage', 'GAD'], required_words=['manage', 'GAD'])
        response("Stress can be managed through techniques like deep breathing, exercise, and time management. It's important to find what works best for you.", ['how', 'to', 'reduce', 'stress'], required_words=['reduce', 'stress'])
        response("Stress can be managed through techniques like deep breathing, exercise, and time management. It's important to find what works best for you.", ['how', 'to', 'reduce', 'stress'], required_words=['reduce', 'stress'])
        response("Mindful journaling is a practice that involves expressing your thoughts and feelings in a non-judgmental way. It can help improve mental clarity.", ['how', 'to', 'start', 'mindful', 'journaling'], required_words=['start', 'mindful', 'journaling'])
        response("Seeking help for mental health concerns is a sign of strength, not weakness. Professionals are trained to support and guide you.", ['why', 'is', 'seeking', 'help', 'important'], required_words=['seeking', 'help'])
        response("Mindful journaling is a practice that involves expressing your thoughts and feelings in a non-judgmental way. It can help improve mental clarity.", ['how', 'to', 'start', 'mindful', 'journaling'], required_words=['start', 'mindful', 'journaling'])
        response("Body image and self-acceptance are important for mental health. Focus on self-love and your inner qualities rather than appearance.", ['how', 'to', 'improve', 'body', 'image', 'and', 'self-acceptance'], required_words=['improve', 'body', 'image', 'self-acceptance'])
        response("Practicing gratitude can boost mental well-being. Start by keeping a gratitude journal to appreciate the positives in your life.", ['what', 'are', 'the', 'benefits', 'of', 'gratitude'], required_words=['benefits', 'gratitude'])
        response("Obsessive-Compulsive Disorder (OCD) can be managed with therapy and medication. Exposure and response prevention is a common treatment approach.", ['how', 'to', 'manage', 'OCD'], required_words=['manage', 'OCD'])
        response("Setting boundaries is essential for maintaining good mental health. Communicate your limits clearly to avoid burnout.", ['how', 'to', 'set', 'boundaries', 'for', 'mental', 'health'], required_words=['set', 'boundaries', 'mental', 'health'])

        best_match = max(highest_prob_list, key=highest_prob_list.get)
        return "Unknown" if highest_prob_list[best_match] < 1 else best_match

    def get_response(self, user_input):
        split_message = re.split(r'\s+|[,;?!.-]\s*', user_input.lower())
        response = self.check_all_messages(split_message)
        return response

def response_api(prompt):
    response = Bard().get_answer(str(prompt))
    print(response)  # Add this line to print the response to the console
    message = response['content']
    return message


def main():
    st.title("🌡️ Health Chatbot Interface 🏥")

    chatbot = ChatBot()

    st.markdown(
        f"""
        <style>
            .stApp {{
                background: linear-gradient(135deg, #e6e6fa, #c4c4ff);
                color: black;
                padding: 1rem;
                border-radius: 10px;
                width: 100%;
                height: 100%;
            }}
        </style>
        """,
        unsafe_allow_html=True,
    )
    
    user_input = st.text_input("You:")

    if st.button("Submit"):
        response = chatbot.get_response(user_input)
        
        # Check if the response is unknown and use Bard API in that case
        if response == "Unknown":
            bard_response = response_api(user_input)
            st.markdown(f"**Bot:** {bard_response}", unsafe_allow_html=True)
        else:
            st.markdown(f"**Bot:** {response}", unsafe_allow_html=True)

if __name__ == "__main__":
    main()
