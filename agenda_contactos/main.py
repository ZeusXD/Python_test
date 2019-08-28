from contact_book import ContactBook


def run():
    
    contact_book = ContactBook()

    contact_book.read_csv()

    while True:
        command = str(input('''
            Â¿QuÃ© deseas hacer?

            [a]ñadir contacto
            [ac]tualizar contacto
            [b]uscar contacto
            [e]liminar contacto
            [l]istar contactos
            [s]alir
        '''))

        if command == 'a':
            name = str(input('Escribe el nombre: '))
            phone = str(input('Escribe el telefono: '))
            email = str(input('Escribe el email: '))

            contact_book.add(name,phone,email)

        elif command == 'ac':
            name = str(input('Escribe el nombre: '))
            contact_book.update(name)

        elif command == 'b':
            name = str(input('Escribe el nombre: '))
            contact_book.search(name)

        elif command == 'e':
            name = str(input('Escribe el nombre: '))
            contact_book.delete(name)

        elif command == 'l':
            contact_book.show_all()

        elif command == 's':
            break
        else:
            print('Comando no encontrado.')


if __name__ == '__main__':
    run()