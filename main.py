import streamlit as st
import pandas as pd
import random
from PIL import Image

def main():

    # Excel空過去問を読み込みしデータフレームに格納
    df = pd.read_excel("test.xlsx")

    # タイトルを表示
    st.markdown('# 土木鋼構造診断士・診断士補の択一問題　過去問をひたすら解く💪（試作版）')
    st.markdown('#### 👈サイドバーから解きたい過去問の年度を選択できます。')

    # 県別のセレクトボックスを作成する
    year_list = df['年度'].unique()
    selected_year = st.sidebar.multiselect(
        '◇解きたい過去問の年度を選択（複数選択可）：',
        year_list
    )

    #　セレクトされた国でデータフレームの中身をフィルタリングする##
    df = df [df['年度'].isin(selected_year)]
    
    # 問題番号を選択
    l_index = list(df.index)
    q_no = df.index[random.randint(0, len(l_index) - 1)]

    # 問題を表示
    st.markdown('## ◇問題')
    st.write(int(df["年度"][q_no]), "年度問題：問題番号", int(df["問題番号"][q_no]))
    st.write(str(df["問題文"][q_no]))

    # 問題画像を表示
    if  df["問題画像フラグ"][q_no] == 1:
        image = Image.open("image/" + str(df["問題画像ファイル名"][q_no]) + '.JPG')
        st.image(image, use_column_width=False)
    else:
        pass
    
    # 回答選択肢を表示
    st.write('1)　' + str(df["選択肢１"][q_no]))
    st.write('2)　' + str(df["選択肢２"][q_no]))
    st.write('3)　' + str(df["選択肢３"][q_no]))
    st.write('4)　' + str(df["選択肢４"][q_no]))

    # 解答を表示
    st.markdown('## ◇解答')
    with st.beta_expander('解答を表示'):
        st.write(int(df["正解"][q_no]))
    # 解説を表示
    st.markdown('## ◇解説')
    with st.beta_expander('解説を表示'):
        st.write(str(df["解説"][q_no]))
        # 解説画像を表示
        if df["解説画像フラグ"][q_no] == 1:
            image = Image.open("image/" + str(df["解説画像ファイル名"][q_no]) + '.JPG')
            st.image(image, use_column_width=False)
        else:
            pass

    # リロードボタン
    st.write('⚠️次の問題の前に、解答表示、解説表示を閉じること')
    st.button('次の問題へ')


if __name__ == '__main__':
    main()