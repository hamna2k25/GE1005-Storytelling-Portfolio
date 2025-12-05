# GE1005-Storytelling-Portfolio
My GE1005 Communication &amp; Storytelling Portfolio
GE1005-Storytelling-Portfolio/
│
├── Stories/        # Your essays or stories
├── Images/         # Illustrations, screenshots, posters
├── Code/           # Optional Python scripts (word counter, etc.)
├── Reflections.md  # Your reflections after each story
└── About.md        # About you: name, student ID, contact info

Stories/story1.md
Stories/story2.pdf

Images/story1_poster.png
Images/story2_diagram.jpg


# Reflections

## Story 1: The Power of Words
- What I learned: Clear communication makes ideas stronger.
- Challenges: Choosing the right tone for storytelling.
- Improvements: Plan story structure better next time.

## Story 2: My Creative Essay
- What I learned: Visual descriptions help engage the reader.
- Challenges: Limited vocabulary for some topics.
- Improvements: Read more to expand vocabulary.

- # About Me

- **Name:** Hamna
- **Student ID:** 123456
- **Course:** GE1005 – Communication: The Power of Words
- **Contact:** hamna@email.com
- **Interests:** Storytelling, digital communication, creative writing


def count_words(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        text = f.read().lower()
    words = text.split()
    freq = {}
    for w in words:
        freq[w] = freq.get(w, 0) + 1
    return freq

if __name__ == "__main__":
    file = "Stories/story1.md"
    frequencies = count_words(file)
    print("Word Frequency in your story:\n")
    for word, count in frequencies.items():
        print(f"{word}: {count}")

# GE1005 Storytelling Portfolio

This repository is my portfolio for GE1005 – Communication: The Power of Words.  
It includes stories, reflections, illustrations, and optional analysis scripts.

## Folders

- **Stories/**: Essays and creative writing
- **Images/**: Posters, diagrams, screenshots
- **Code/**: Optional Python scripts (e.g., word frequency counter)
- **Reflections.md**: Reflections on each story
- **About.md**: Information about me

## How to Use

1. Read the stories in Stories/ folder.
2. View images in Images/ folder.
3. Run any Python scripts in Code/ for interactive analysis.
4. Read Reflections.md for my personal insights.



