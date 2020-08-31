#include "lists.h"

/**
 * insert_node - a program to insert a new node in a sorted linked list
 * @head: a pointer to the head of the list
 * @number: an int for our new node
 * Return: Pointer to new node or NULL for any failure
 */

listint_t *insert_node(listint_t **head, int number)
{
  listint_t *new_node;
  listint_t *mover;

  /* If the head pointer is null or number is null, return null  */
  if (*head == NULL)
    return (NULL);
  /* Else we need a pointer to manipulats so mover = head of list */
  mover = *head;
  /* Make our new node by mallocing, if fails return null */
  new_node = malloc(sizeof(listint_t));
  if (new_node == NULL)
    return (NULL);
  /* Assign our number value to new node */
  new_node->n = number;
  /* If number is less than the n in head, point 
     new_node at head and assign head new_node */
  if (number < mover->n)
    {
      new_node->next = mover;
      *head = new_node;
      return (*head);
    }
  /* Otherwise iterate until we run out of list */
  while (mover != NULL)
    {
      /* If the next node n is > new node n*/
      if (mover->next->n > number)
        {
	  new_node->next = mover->next;
	  mover->next = new_node;
	  return (new_node);
        }
      /* If we reach the last node and we have not hit 
	 the above condition, new tail  */
      else if (mover->next == NULL)
        {
	  mover->next = new_node;
	  return (new_node);
        }
      mover = mover->next;
    }
  return (NULL);
}
