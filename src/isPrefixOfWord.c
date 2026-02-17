/* 1455 */

#include <string.h>

int isPrefixOfWord(char *sentence, char *searchWord) {
    int wordIndex = 1;
    int searchLen = strlen(searchWord);
    char *word = strtok(sentence, " ");

    while (word != NULL) {
        if (strncmp(word, searchWord, searchLen) == 0)
            return wordIndex;
        word = strtok(NULL, " ");
        wordIndex++;
    }

    return -1;
}
