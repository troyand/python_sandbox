# -*- coding: utf-8 -*-

def transliterate(input_string, language, transliteration_system):
    from uk_letters import get_transliteration_dict
    mapping = {
            'uk': get_transliteration_dict(transliteration_system)
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
    parser.add_option("-t", "--transliteration", dest="transliteration_system", default="BGN/PCGN",
            help="transliteration system")
    (options, args) = parser.parse_args()

    print transliterate(unicode(options.input_string, 'utf-8'), options.language, options.transliteration_system)

if __name__=="__main__":
    main()
