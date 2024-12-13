def is_valid(state):
    """Periksa apakah kondisi valid."""
    left, right, _ = state
    left_missionaries, left_cannibals = left
    right_missionaries, right_cannibals = right

    # Pastikan misionaris tidak kalah jumlah di kedua sisi sungai
    if (left_missionaries < left_cannibals and left_missionaries > 0) or \
       (right_missionaries < right_cannibals and right_missionaries > 0):
        return False
    return True

def move(state, missionaries, cannibals):
    """Lakukan perpindahan dan periksa validitas."""
    left, right, boat = state
    if boat == 'left':
        # Pindahkan dari kiri ke kanan
        new_left = [left[0] - missionaries, left[1] - cannibals]
        new_right = [right[0] + missionaries, right[1] + cannibals]
        new_boat = 'right'
    else:
        # Pindahkan dari kanan ke kiri
        new_left = [left[0] + missionaries, left[1] + cannibals]
        new_right = [right[0] - missionaries, right[1] - cannibals]
        new_boat = 'left'

    # Bentuk status baru
    new_state = [new_left, new_right, new_boat]

    # Pastikan status baru valid
    if min(new_left) < 0 or min(new_right) < 0 or not is_valid(new_state):
        return None
    return new_state

def display_state(state):
    """Tampilkan status saat ini."""
    left, right, boat = state
    print("\nSisi Kiri: " + "M" * left[0] + "K" * left[1])
    print("Perahu:", "Kiri" if boat == "left" else "Kanan")
    print("Sisi Kanan: " + "M" * right[0] + "K" * right[1])

def check_game_over(state, new_state):
    """Periksa apakah langkah menyebabkan Game Over."""
    if new_state is None:
        return "Game Over!"
    left, right, _ = new_state
    left_missionaries, left_cannibals = left
    right_missionaries, right_cannibals = right

    if left_missionaries < left_cannibals and left_missionaries > 0:
        return "Game Over! Kanibal melebihi misionaris di sisi kiri."
    if right_missionaries < right_cannibals and right_missionaries > 0:
        return "Game Over! Kanibal melebihi misionaris di sisi kanan."
    return None

def get_input(prompt):
    """Dapatkan input angka atau keluar ('c')."""
    user_input = input(prompt)
    if user_input.lower() == 'c':
        return 'c'
    try:
        value = int(user_input)
        if 0 <= value <= 2:
            return value
        else:
            print("Masukkan angka antara 0 dan 2. Coba lagi!")
            return None
    except ValueError:
        print("Masukan harus berupa angka atau 'c'. Coba lagi!")
        return None

def main():
    """Permainan Missionaries and Cannibals."""
    state = [[3, 3], [0, 0], 'left']  # Status awal
    goal_state = [[0, 0], [3, 3], 'right']  # Status akhir

    print("Permainan Missionaries and Cannibals")
    print("Aturan:")
    print("- Maksimal 2 orang bisa naik perahu.")
    print("- Misionaris tidak boleh kalah jumlah dari kanibal di sisi mana pun.")
    print("- Langkah tidak valid akan menyebabkan Game Over.")
    print("- Tujuan: Pindahkan semua ke sisi kanan.")
    print("- Masukkan 'c' untuk keluar dari permainan.")

    while state != goal_state:
        display_state(state)

        print("\nMasukkan jumlah misionaris dan kanibal yang akan dipindahkan:")
        missionaries = get_input("Misionaris (0-2): ")
        if missionaries == 'c':
            print("Permainan dihentikan. Terima kasih telah bermain!")
            return

        cannibals = get_input("Kanibal (0-2): ")
        if cannibals == 'c':
            print("Permainan dihentikan. Terima kasih telah bermain!")
            return

        if missionaries is None or cannibals is None:
            continue

        if missionaries + cannibals > 2 or missionaries + cannibals < 1:
            print("Perahu hanya dapat membawa 1 atau 2 orang. Langkah ini tidak valid!")
            print("Game Over! Langkah tidak valid.")
            return

        # Coba langkah baru
        new_state = move(state, missionaries, cannibals)

        # Periksa apakah langkah menyebabkan Game Over
        game_over_reason = check_game_over(state, new_state)
        if game_over_reason:
            print(f"\n{game_over_reason}")
            return

        # Perbarui status jika langkah valid
        state = new_state

    print("\nSelamat! Anda berhasil memindahkan semua ke sisi kanan.")
    display_state(state)

if __name__ == "__main__":
    main()
