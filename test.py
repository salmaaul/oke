import streamlit as st

def electron_configuration(atom_number):
    electrons = atom_number
    config = ""
    shell = 1

    while electrons > 0:
        max_electrons = 2 * shell ** 2
        if electrons >= max_electrons:
            config += f"{max_electrons} {shell}s "
            electrons -= max_electrons
        else:
            config += f"{electrons} {shell}s "
            electrons = 0
        shell += 1

    return config.strip()

def main():
    st.title("Aplikasi Konfigurasi Elektron")

    atom_number = st.number_input("Masukkan nomor atom:", min_value=1, value=1, step=1)

    if st.button("Tampilkan Konfigurasi Elektron"):
        config = electron_configuration(atom_number)
        st.write(f"Konfigurasi elektron untuk atom nomor {atom_number} adalah: {config}")

if _name_ == "_main_": 
    main()