#include "lists.h"

/**
 * is_palindrome - a function to see if a list is a palindrome
 * @head: the head of a singly linked list
 * Return: 1 is yes or 0 if no.
 **/

int is_palindrome(listint_t **head)
{
    listint_t *mover;
    int end = 0;
    int start = 0;
    int thelist[1024]; 

    if ((*head) == NULL)
        return (1);
    mover = (*head);
    while (mover != NULL)
    {
        thelist[end] = mover->n;
        mover = mover->next;
        end++;
    }
    if (end == 1)
        return (1);
    end--;
    while (end >= start)
    {
        if (thelist[start] == thelist[end])
        {
            start++;
            end--;
        }
        else
        {
            return (0);
        }
    }
    return (1);
}
