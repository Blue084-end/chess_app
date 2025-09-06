import streamlit as st
from game import Game

st.set_page_config(layout="wide")
game = Game()

st.title("🧨 Cờ Tướng Web App")

# Hiển thị bàn cờ
for row in range(10):
    cols = st.columns(9)
    for col in range(9):
        piece = game.board.grid[row][col]
        if piece:
            img_path = f"assets/{piece.color}/{piece.name}.png"
            cols[col].image(img_path, use_column_width=True)
        else:
            cols[col].empty()

# Nhập nước đi
from_pos = st.text_input("Từ ô (vd: 0,0)")
to_pos = st.text_input("Đến ô (vd: 2,0)")
if st.button("Đi quân"):
    game.make_move(eval(from_pos), eval(to_pos))

if st.button("Ván mới"):
    game.restart()

