import streamlit as st

# Sample dataset (replace this with your own dataset)
dataset = [
    {"question": "Memuji Orang di Jalanan", "answer": "仁", "jawaban": "Mencintai"},
    {"question": "Membantu Orang Tua Menyebrang Jalan", "answer": "悌","jawaban": "Menghormati"},
    {"question": "Berdana Kepada Orang yang Membutuhkan", "answer": "仁","jawaban": "Bersyukur"},
    # Add more questions and answers as needed
]

def print_random_data(data):
    random_data = random.choice(data)
    print("Hello! New Challenge!\nLakukan satu kebaikan di bawah ini!\n",random_data['question'])
    return random_data

def main():
    while True:
        user_input = input("Apakah kamu berhasil melakukan challengenya? (Ya/Tidak)")

        # Replace this condition with your own boolean condition
        if user_input.lower() == "ya":
            print("Nice! Very proud of you!")
            break  # Exit the loop if the condition is true
        else:
            print("Ayo coba lagi sampai bisa! (Ketik 'Ya' apabila kamu telah berhasil!)")


def quiz(random_data):
    user_answer = input("QUIZ! Sekarang ayo coba tebak, kira-kira nilai konfusius apa yang berhubungan dengan kebaikan yang barusan dilakukan!").strip()
    correct_answer = random_data['answer']

    if user_answer.lower() == correct_answer.lower():
        print("Kelass, benar sekali!")
    else:
        print(f"Belum tepat, jawaban benarnya adalah:{correct_answer}")

def jawaban(random_data):
    user_answerr = input("Lanjuttt, sekarang kira-kira apa nilai humanis yang berhubungan dengan kebaikan yang barusan dilakukan?").strip()
    correct_answerr = random_data['jawaban']

    if user_answerr.lower() == correct_answerr.lower():
        print("Kerenn, 100 untuk Anda!")
    else:
        print(f"Kurang tepat , jawaban benarnya adalah:{correct_answerr}")

if __name__ == "__main__":
    random_data = print_random_data(dataset)
    main()
    quiz(random_data)
    jawaban(random_data)

import random

# Sample dataset (replace this with your own dataset)
datasett = [
    "父母呼 应勿缓 父母命 行勿懒 (fù mǔ hū, yìng wù huǎn, fù mǔ mìng, xíng wù lǎn)\nBila orang tua memanggil, cepat menyahut jangan lamban. Bila orang tua memberi tugas, cepat mengerjakan jangan malas.",
    "父母教 须敬听 父母责 须顺承 (fù mǔ jiào, xū jìng tīng, fù mǔ zé, xū shùn chéng)\nBila orang tua memberi nasihat, simaklah dengan saksama dan syukur. Bila orang tua menegur, turutilah dan terima dengan ikhlas.",
    "冬则温 夏则凊 晨则省 昏则定 (dōng zé wēn, xià zé jìng, chén zé xǐng, hūn zé ding)\nBeri orang tua kehangatan di musim dingin, berilah kesejukan di musim panas. Beri salam di pagi hari, beri ketenangan di malam hari (agar orang tua dapat tidur tenang).",
    # Add more data as needed
]

def print_random_data(data):
    random_data = random.choice(data)
    print("Congrats! Anda telah menyelesaikan challenge hari ini dengan baik! Selamat menjalani harimu :D ! \n",random_data)

# Call the function to print random data from the dataset
print_random_data(datasett)
