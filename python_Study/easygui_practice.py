import easygui
flavor = easygui.buttonbox("What is your favorite ice cream flavor?",
                           choices = ['Vanilla', 'Chocolate', 'Strawberry'])
flavor2 = easygui.choicebox("What is your favorite ice cream flavor?",
                            choices = ['Vanilla', 'Chocolate', 'Strawberry'])
flavor3 = easygui.enterbox("What is your favorite ice cream flavor?", default = 'vanilla')
easygui.msgbox("You picked " + flavor3)
