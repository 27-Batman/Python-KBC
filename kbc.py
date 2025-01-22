questions = ("What is the capital of Nepal?",
             "Which mountain is the highest peak in the world?",
             "What is Nepal's national animal?",
             "What is Nepal's national flower?",
             "Which city is known as the 'City of Lakes' in Nepal?",
             "Who wrote the Nepali national anthem 'Sayaun Thunga Phoolka'?",
             "Which is the smallest district in Nepal by area?",
             "When was Nepal declared a federal democratic republic?",
             "Which river is the longest in Nepal?",
             "Which is the largest lake in Nepal?",
             "Which festival in Nepal is known as the 'Festival of Lights'?",
             "Which place in Nepal is a UNESCO World Heritage Site and the birthplace of Lord Buddha?",
             "Which Nepali sport is traditionally played during Dashain?",
             "What is the full form of 'NAC,' the national flag carrier airline of Nepal?",
             "What is the height of Mount Everest in meters?",)

options = (("A. Kathmandu", "B. Pokhara", "C. Lalitpur", "D. Biratnagar"),
           ("A. Kanchenjunga", "B. Lhotse", "C. Everest", "D. Makalu"),
           ("A. Cow", "B. Tiger", "C. Red Panda", "D. Snow Leopard"),
           ("A. Rhododendron", "B. Lotus", "C. Sunflower", "D. Lily"),
           ("A. Kathmandu", "B. Pokhara", "C. Chitwan", "D. Lumbini"),
           ("A. Byakul Maila", "B. Madhav Prasad Ghimire", "C. Bhanu Bhakta Acharya", "D. Laxmi Prasad Devkota"),
           ("A. Bhaktapur", "B. Lalitpur", "C. Manang", "D. Dolpa"),
           ("A. 2006", "B. 2008", "C. 2010", "D. 2012"),
           ("A. Koshi", "B. Karnali", "C. Gandaki", "D. Bagmati"),
           ("A. Rara Lake", "B. Tilicho Lake", "C. Phewa Lake", "D. Begnas Lake"),
           ("A. Dashain", "B. Tihar", "C. Holi", "D. Maghe Sankranti"),
           ("A. Lumbini", "B. Janakpur", "C. Muktinath", "D. Gorkha"),
           ("A. Dandi Biyo", "B. Kho Kho", "C. Kabaddi", "D. Volleyball"),
           ("A. Nepal Aviation Company", "B. Nepal Airlines Corporation", "C. National Aviation Corporation", "D. Nepal Airways Charter"),
           ("A. 8848.86 m", "B. 8849.86 m", "C. 8847.86 m", "D. 8846.86 m"))

prizes = ("Rs. 1,000",
          "Rs. 2,000",
          "Rs. 5,000",
          "Rs. 10,000",
          "Rs. 20,000",
          "Rs. 40,000",
          "Rs. 80,000",
          "Rs. 1,60,000",
          "Rs. 3,20,000",
          "Rs. 6,40,000",
          "Rs. 12,50,000",
          "Rs. 25,00,000",
          "Rs. 50,00,000",
          "Rs. 1,00,00,000",
          "Rs. 7,00,00,000",)

answers = ("A", "C", "A", "A", "B", "A", "A", "B", "B", "A", "B", "A", "A", "B", "A")
used_lifeline = False
prize_won = "Rs. 0"

print("\n--Welcome to KBC--\n"
      "Ko Bancha Corepati!\n")
print("Rules:\n"
      "- You’ll have 15 questions to answer.\n"
      "- Each correct answer will increase your prize.\n"
      "- You have one lifeline: 50:50, which eliminates two incorrect options.\n"
      "- Type 'L' to use the lifeline (only once).\n"
      "- Type 'Q' to quit and take home your winnings.\n")
print("Prizes for each question:")
for i, prize in enumerate(prizes):
    print(f"Q{i + 1}: {prize}")
print("\nGood luck!\n")

for i, question in enumerate(questions):
    print(f"--------------------\nQn {i + 1}: {question}")
    for option in options[i]:
        print(option)

    if not used_lifeline:
        print("\nType 'L' to use your lifeline.")

    answer = input("\nEnter your answer (A, B, C, D), 'L' for lifeline, or 'Q' to quit: ").upper()

    if answer == "L" and not used_lifeline:
        used_lifeline = True
        correct_answer = answers[i]
        option_dict = {opt[0]: opt[3:] for opt in options[i]}
        wrong_options = [opt for opt in "ABCD" if opt != correct_answer][:2]
        print("\nOptions after 50:50:")
        print(f"{correct_answer}. {option_dict[correct_answer]} | {wrong_options[0]}. {option_dict[wrong_options[0]]}")
        answer = input("\nEnter your answer (A, B, C, D): ").upper()

    if answer == "Q":
        print(f"You quit the game. You take home {prize_won}.")
        break

    if answer == answers[i]:
        prize_won = prizes[i]
        print(f"Correct! You won {prizes[i]}!")
    else:
        print("Incorrect! You lose all your winnings.")
        prize_won = "Rs. 0"
        break