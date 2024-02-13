import streamlit as st
import random

st.set_page_config(page_title="1 Hari 1 Kebaikan", page_icon=":star:", layout="wide")

dataset = [
    {"question": "Memuji Orang di Jalanan", "answer": "仁", "jawaban": "Mencintai"},
    {"question": "Membantu Orang Tua Menyebrang Jalan", "answer": "悌","jawaban": "Menghormati"},
    {"question": "Berdana Kepada Orang yang Membutuhkan", "answer": "仁","jawaban": "Bersyukur"},
]

datasett = [
    "父母呼 应勿缓 父母命 行勿懒 (fù mǔ hū, yìng wù huǎn, fù mǔ mìng, xíng wù lǎn)\nBila orang tua memanggil, cepat menyahut jangan lamban. Bila orang tua memberi tugas, cepat mengerjakan jangan malas.",
    "父母教 须敬听 父母责 须顺承 (fù mǔ jiào, xū jìng tīng, fù mǔ zé, xū shùn chéng)\nBila orang tua memberi nasihat, simaklah dengan saksama dan syukur. Bila orang tua menegur, turutilah dan terima dengan ikhlas.",
    "冬则温 夏则凊 晨则省 昏则定 (dōng zé wēn, xià zé jìng, chén zé xǐng, hūn zé ding)\nBeri orang tua kehangatan di musim dingin, berilah kesejukan di musim panas. Beri salam di pagi hari, beri ketenangan di malam hari (agar orang tua dapat tidur tenang).",
]

def print_random_data(data):
    random_data = random.choice(data)
    st.write("Hello! New Challenge!\nLakukan satu kebaikan di bawah ini!\n",random_data['question'])

def main():
    user_input = st.text_input("Apakah kamu berhasil melakukan challengenya? (Ya/Tidak)")

    if user_input.lower() == "ya":
        st.write("Nice! Very proud of you!")
    elif user_input.lower() == "tidak":
        st.write("Ayo coba lagi sampai bisa! (Ketik 'Ya' apabila kamu telah berhasil!)")

def quiz(random_data):
    user_answer = st.text_input("QUIZ! Sekarang ayo coba tebak, kira-kira nilai konfusius apa yang berhubungan dengan kebaikan yang barusan dilakukan?").strip()
    correct_answer = random_data['answer']

    if user_answer.lower() == correct_answer.lower():
        st.write("Kelass, benar sekali!")
    else:
        st.write(f"Belum tepat, jawaban benarnya adalah:{correct_answer}")

def jawaban(random_data):
    user_answerr = st.text_input("Lanjuttt, sekarang kira-kira apa nilai humanis yang berhubungan dengan kebaikan yang barusan dilakukan?").strip()
    correct_answerr = random_data['jawaban']

    if user_answerr.lower() == correct_answerr.lower():
        st.write("Kerenn, 100 untuk Anda!")
    else:
        st.write(f"Kurang tepat , jawaban benarnya adalah:{correct_answerr}")

def app():
    st.title("My Streamlit App")
    random_data = print_random_data(dataset)
    main()
    quiz(random_data)
    jawaban(random_data)

if __name__ == "__main__":
    app()
