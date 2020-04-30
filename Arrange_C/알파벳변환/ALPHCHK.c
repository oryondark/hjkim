


#include "ALPHCHK.h"
char *check_alph(char alpha){
	char *buf = NULL;
	buf = &alpha;

	int return_value;

	return_value = isalpha(alpha);

	if(return_value != 0){
		printf("set uppercase %c\n", (char)toupper(alpha));
		return buf;
	}
	else{
		printf("Not Alphabet\n");
		return NULL;
	}
}

int input_scan(){
	char alpha;
	char *ret;

	//input
	printf("input character :");
	//scanf("%c", &alpha);
	gets(&alpha);
	//is Alphabet??
	ret = check_alph(alpha);
	if( ret == NULL ){
		return 0;
	}

	return 1;
}


void main(int argc, char **argv){
	int ret2;
	printf("*** 14931480 KIMHYUNJUNE report	***\n");
	while(1){
		ret2 = input_scan();
		if(ret2 == 1)
			break;
	}




}
