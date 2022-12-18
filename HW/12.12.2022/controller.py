import logger
import model
import view

def run():
    while True:
        mode = view.choose_mode()
        if mode == '1':
            contact = view.new_contact()
            logger.add_new(contact)
        elif mode == '2':
            contact = view.contact_to_s()
            base = logger.get_base()
            result = model.search_contact(base, contact)
            view.show_found(result)

