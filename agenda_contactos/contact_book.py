from contact import Contact
import csv

class ContactBook:

    def __init__(self):
        self._contacts = []

    def add(self, name, phone, email):
        contact = Contact(name,phone,email)
        self._contacts.append(contact)
        self._save()
        # print('name: {}, phone: {}, email: {}'.format(name, phone, email))
    
    def show_all(self):
        for contact in self._contacts:
            self._print_contact(contact)

    def delete(self,name):#enumerate devuelve el indice, obj
        for idx, contact in enumerate(self._contacts):
            if contact.name.lower() == name.lower():
                del self._contacts[idx]
                print('Contacto "{}" eliminado'.format(name))
                self._save()
                break
        else:
            self._not_found_contact()

    def search(self,name):
        for contact in self._contacts:
            if contact.name.lower() == name.lower():
                self._print_contact(contact)
                break
        else:#del loop el cual si termina y no hay break
            self._not_found_contact()

    def update(self,name):
        for contact in self._contacts:
            if contact.name.lower() == name.lower():
                self._update_contact_data(contact)
                print('Contacto actualizado!!')
                self.search(contact.name)
                self._save()
                break
        else:
            self._not_found_contact()

    def read_csv(self):
        with open('contacts.csv','r') as f:
            reader = csv.reader(f)
            for idx, row in enumerate(reader):
                if idx == 0:
                    continue

                if(row != []):
                    self.add(row[0],row[1],row[2])


    def _print_contact(self, contact):
        print('--- * --- * --- * --- * --- * --- * --- * ---')
        print('Nombre: {}'.format(contact.name))
        print('Teléfono: {}'.format(contact.phone))
        print('Email: {}'.format(contact.email))
        print('--- * --- * --- * --- * --- * --- * --- * ---')

    def _not_found_contact(self):
        print('**********')
        print('No encontrado!')
        print('**********')
    
    def _update_contact_data(self,contact):
        new_name = str(input('Nuevo nombre: '))
        new_phone = str(input('Nuevo telefono: '))
        new_email =str(input('Nuevo email: '))

        contact.name = new_name if new_name != '' else contact.name
        contact.phone = new_phone if new_phone != '' else contact.phone
        contact.email = new_email if new_email != '' else contact.email

    def _save(self):
        with open('contacts.csv','w',newline='') as f:
            writer = csv.writer(f)
            writer.writerow(('name','phone','email'))

            for contact in self._contacts:
                writer.writerow((contact.name,contact.phone,contact.email))