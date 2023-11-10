import sys

def gener_count(input_file, output_file):
    count_genre = {} #각 genre을 count하는 딕셔너리

    print("Input File:", input_file)
    print("Output File:", output_file)

    with open(input_file, 'r', encoding='utf-8') as openf:
        for lines in openf:
            line = lines.split("::")
            movies_genre = line[2].split("|")
            for genre in movies_genre:
                if genre in count_genre:
                    count_genre[genre] += 1
                else:
                    count_genre[genre] = 1

    with open(output_file, 'w', encoding='utf-8') as outf:
        for genre, count in count_genre.items():
            outf.write("%s %d\n" % (genre, count))

print("Command Line Arguments:", sys.argv)

input_file = sys.argv[1]
output_file = sys.argv[2]

gener_count(input_file, output_file)