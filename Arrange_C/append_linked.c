void Append(struct linkedList **prev, const char *name, char *item){
	//해당 함수가 호출될 때 받는 인자는 분류할 name 명과 추출한 item 명
	linkedList *new_node = NULL;
	linkedList *ptr_node = NULL;


	ptr_node = *prev;


	int item_len = strlen(item);
	int name_len = strlen(name);
	char itemBuf[item_len];
	char nameBuf[name_len];

	sprintf(nameBuf, "%s", name); 
	sprintf(itemBuf, "%s", item);

	/* 신규 노드 생성 */
	//print("%s : %s\n", itemBuf, nameBuf);
	new_node = (linkedList *) malloc(sizeof(linkedList)); 
	memcpy(new_node->name, nameBuf, name_len + 1); 
	memcpy(new_node->item, itemBuf, item_len + 1); 
	new_node->next = NULL;


	if (*prev == NULL){
		*prev = new_node;
		return;
	}
	while(ptr_node->next != NULL){
		ptr_node = ptr_node->next;
	}

	//링크드 리스트 가장 끝에  신규 노드 추가
	ptr_node->next = new_node;
	return;
}