# QUIZ

print('Press 1, 2 to Choose answer')
print('Level 1: Easy')

option_Q_1 = '1.Nicola Tesla 2.The Right Brothers'
print(option_Q_1)

Q_1 = int(input('Q1. Who invented Plane? :'))

if Q_1 == 2:
    print('Correct')

    option_Q_2 = '1.Tesla 2.BMW'
    print(option_Q_2)
    Q_2 = int(input('Q2. Which Company made the worlds first self driving car? :'))

    if Q_2 == 1:
        print('Correct')

        option_Q_3 = '1.Half Amarican 2.Half Bangladeshi'
        print(option_Q_3)
        Q_3 = int(input("Q3. Youtube's Creator Jawed is Half______. :"))

        if Q_3 == 2:
            print('Correct')
            print('You passed Level 1')
            print("")
            print('Level 2: Intermidiate')

            option_Q_4 = '1.Steve Jobs and Steve Wasniak 2.Steve Jobs and Steve Rebrican'
            print(option_Q_4)
            Q_4 = int(input('Q4. Who Created Apple? :'))

            if Q_4 == 1:
                print('Correct')

                option_Q_5 = '1.Homo Sapiens 2.Humo Sapiens'
                print(option_Q_5)
                Q_5 = int(input('Q5. What is the Scientific name of Humans? :'))

                if Q_5 == 1:
                    print('Correct')

                    option_Q_6 = '1.World Wide Web 2.World Wide Website'
                    print(option_Q_6)
                    Q_6 = int(input('Q6. what does www mean? :'))

                    if Q_6 == 1:
                        print('Correct')
                        print('You passed Level 2')
                        print("")
                        print('Level 3: Hard')

                        option_Q_7 = '1.Samsung 2.Google'
                        print(option_Q_7)
                        Q_7 = int(input('Q7. Who ones Android :'))

                        if Q_7 == 2:
                            print('Correct')

                            option_Q_8 = '1.Apple 2.T-Mobile'
                            print(option_Q_8)
                            Q_8 = int(input('Q8. Who invented the first smartphone? :'))

                            if Q_8 == 1:
                                print('Correct')

                                option_Q_9 = '1.wifi 2.Blutooth'
                                print(option_Q_9)
                                Q_9 = int(input('Which Technology is used in wireless Mouses: '))

                                if Q_9 == 2:
                                    print('Correct')
                                    print('You passed Level 3')
                                    print("")
                                    print('Bonus Question')

                                    option_Q_10 = '1.Global Positioning System 2.Global Positioning Source'
                                    print(option_Q_10)
                                    Q_10 = int(input('What is the full Form of GPS? :'))

                                    if Q_10 == 1:
                                        print('Correct')
                                        print('You Are the winner!!!')
                                        print('Points: 10')

                                    else:
                                        print('Wrong Answer')
                                        print('Game Over')
                                        print('Points: 9')
  
                                else:
                                    print('Wrong Answer')
                                    print('Game Over')
                                    print('Points: 8')
                            
                            else:
                                print('Wrong Answer')
                                print('Game Over')
                                print('Points: 7')

                        else:
                            print('Wrong Answer')
                            print('Game Over')
                            print('Points: 6')

                    else:
                        print('Wrong Answer')
                        print('Game Over')
                        print('Points: 5')

                else:
                    print('Wrong Answer')
                    print('Game Over')
                    print('Points: 4')

            else:
                print('Wrong Answer')
                print('Game Over')
                print('Points: 3')

        else:
            print('Wrong Answer')
            print('Game over')
            print('Points: 2')

    else:
        print('Wrong Answer')
        print('Game over')
        print('Points: 1')
else:
    print('Wrong Answer')
    print('Game over')
    print('Points: 0')