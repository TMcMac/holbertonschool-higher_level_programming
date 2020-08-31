#include "lists.h"

/**
 * check_cycle - a function to check if a singly linked list is cyclical
 * @list: a pointer to the head of a list
 * Return: 0 for staright list or 1 for cyclical list
 */

int check_cycle(listint_t *list)
{
    int count = 0;
    listint_t *mover = list;
  
    while (mover != NULL)
    {
      if (mover == list && count != 0)
	return 1;
      mover = mover->next;
      count++;
    }
    return 0;
}
