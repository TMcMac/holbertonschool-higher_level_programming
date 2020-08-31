#include "lists.h"

/**
 * check_cycle - a function to check if a singly linked list is cyclical
 * @list: a pointer to the head of a list
 * Return: 0 for straight list or 1 for cyclical list
 */

int check_cycle(listint_t *list)
{
    int count = 0;
    listint_t *mover;
    listint_t *trailer;
    
    /* If list is Null or only one node it isn't cyclical */
    if (list == NULL || list->next == NULL)
      return 0;

    /* Trailer starts at head and mover at next node*/
    trailer = list;
    mover = trailer->next;

    /* If mover reaches a null, the list isn't cyclical */
    while (mover != NULL)
    {
      /* If mover gets back to head then the list is cyclical */
      if (mover == list && count != 0)
	return 1;
      /* If mover and trailer meet then the list is cyclical */
      else if (mover == trailer)
	return 1;
      /* Mover is jumping two while trailer is moving one, Tortoise and Hare algo */
      if (mover->next == NULL)
	break;
      mover = mover->next->next;
      trailer = trailer->next;
      count++;
    }
    return 0;
}
