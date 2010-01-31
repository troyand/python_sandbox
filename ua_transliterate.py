# -*- coding: utf-8 -*-

def transliterate(input_string, language):
    from uk_letters import letters as uk_l
    mapping = {
            'uk': uk_l
            }
    output_string = input_string
    for letter in mapping['uk']:
        output_string = output_string.replace(letter, mapping['uk'][letter])
    return output_string


def main():
    from optparse import OptionParser
    parser = OptionParser()
    parser.add_option("-s", "--string", dest="input_string",
            help="input string to be transliterated")
    parser.add_option("-l", "--language", dest="language", default="uk",
            help="language of the input string")
    (options, args) = parser.parse_args()

    print transliterate(unicode(options.input_string, 'utf-8'), options.language)

if __name__=="__main__":
    main()
