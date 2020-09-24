def output_txt(file_name):
    """Output srt file into txt with certain format

    Parameters:
        file_name (string): the file_name / path to the srt file

    Effect:
        Generate a processed txt file with the same name as the file_name

    Below is the pattern for the srt file:
    1
    00:00:01,040 --> 00:00:08,320
    and also i think we all know mrs is a

    2
    00:00:04,319 --> 00:00:11,040
    big full of elites especially from the
    """
    with open(file_name, "r", encoding="utf-8") as f:
        output = []
        lines = f.readlines()

        # Get text with steps
        for line in lines[2::3]:
            line = line.replace("\n", " ")
            output.append(line)

        # Save file
        with open(file_name.replace("srt", 'txt'), "w") as g:
            g.writelines(output)


# Example usage
output_txt("captions.srt")
output_txt("captions (1).srt")
output_txt("captions (2).srt")
