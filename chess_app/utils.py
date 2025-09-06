

# utils.py

def parse_position(pos_str):
    try:
        x, y = map(int, pos_str.strip().split(","))
        if 0 <= x < 10 and 0 <= y < 9:
            return (x, y)
    except:
        return None




def analyze_game(move_history):
    st.subheader("📊 Phân tích ván chơi")

    red_moves = 0
    black_moves = 0
    captures = 0

    for i, move in enumerate(move_history):
        from_pos, to_pos, piece_name = move

        # Đếm số lượt mỗi bên
        if i % 2 == 0:
            red_moves += 1
        else:
            black_moves += 1

        # Ước lượng bắt quân (nếu có)
        if "x" in piece_name.lower() or "capture" in piece_name.lower():
            captures += 1

    st.markdown(f"- 🔴 Số lượt bên đỏ: **{red_moves}**")
    st.markdown(f"- ⚫ Số lượt bên đen: **{black_moves}**")
    st.markdown(f"- ⚔️ Số lần bắt quân (ước lượng): **{captures}**")

    # Gợi ý thêm: phân tích nước đi lặp lại, nước đi mạo hiểm, v.v.








