import streamlit as st
from game import Game

import streamlit as st
from game import Game



if game.winner:
    st.success(f"🎉 {game.winner.upper()} thắng ván này!")
    if st.button("Chơi lại"):
        game.restart()
        st.session_state.selected_piece_pos = None
        st.session_state.valid_moves = []
        st.experimental_rerun()


if st.button("↩️ Undo"):
    if game.undo():
        st.session_state.selected_piece_pos = None
        st.session_state.valid_moves = []
        st.experimental_rerun()

if st.button("↪️ Redo"):
    if game.redo():
        st.session_state.selected_piece_pos = None
        st.session_state.valid_moves = []
        st.experimental_rerun()


st.set_page_config(layout="wide")
st.title("🧨 Cờ Tướng Web App")

# Khởi tạo game nếu chưa có
if "game" not in st.session_state:
    st.session_state.game = Game()
if "selected_piece_pos" not in st.session_state:
    st.session_state.selected_piece_pos = None
if "valid_moves" not in st.session_state:
    st.session_state.valid_moves = []

game = st.session_state.game

# Hiển thị bàn cờ
for row in range(10):
    cols = st.columns(9)
    for col in range(9):
        pos = (row, col)
        piece = game.board.get_piece(row, col)
        button_label = " "  # placeholder

        if piece:
            img_path = f"assets/{piece.color}/{piece.name}.png"
            cols[col].image(img_path, use_column_width=True)
            if st.session_state.selected_piece_pos == pos:
                cols[col].markdown("✅", unsafe_allow_html=True)
            if cols[col].button("Chọn", key=f"select_{row}_{col}"):
                if piece.color == game.turn:
                    st.session_state.selected_piece_pos = pos
                    st.session_state.valid_moves = piece.get_valid_moves(game.board)
        else:
            highlight = "🟩" if pos in st.session_state.valid_moves else ""
            if cols[col].button(highlight or " ", key=f"move_{row}_{col}"):
                if st.session_state.selected_piece_pos and pos in st.session_state.valid_moves:
                    success = game.make_move(st.session_state.selected_piece_pos, pos)
                    if success:
                        st.session_state.selected_piece_pos = None
                        st.session_state.valid_moves = []
                        st.experimental_rerun()


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

# main.py

import streamlit as st
from game import Game
from utils import parse_position

st.set_page_config(layout="wide")
st.title("🧨 Cờ Tướng Web App")

if "game" not in st.session_state:
    st.session_state.game = Game()

game = st.session_state.game

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
from_pos_str = st.text_input("Từ ô (vd: 0,0)")
to_pos_str = st.text_input("Đến ô (vd: 2,0)")
if st.button("Đi quân"):
    from_pos = parse_position(from_pos_str)
    to_pos = parse_position(to_pos_str)
    if from_pos and to_pos:
        success = game.make_move(from_pos, to_pos)
        if not success:
            st.warning("Nước đi không hợp lệ hoặc không phải lượt bạn!")
    else:
        st.error("Sai định dạng ô nhập!")

if st.button("Ván mới"):
    game.restart()
    st.experimental_rerun()

