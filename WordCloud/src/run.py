from wordcloud import WordCloud
import matplotlib.pyplot as plt

class WordCloudGenerator:
    def __init__(self, file_path):
        with open(file_path, encoding='utf-8') as f:
            self.text = f.read()

    def run(self, output_path):
        wordCloud = WordCloud(
            background_color='white',
            max_words=100,
            max_font_size=50,
        ).generate(self.text)

        wordCloud.to_file(output_path)

if __name__ == '__main__':
    wcg = WordCloudGenerator('data/movies.txt')
    wcg.run('output.png')