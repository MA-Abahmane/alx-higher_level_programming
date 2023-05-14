#include "lists.h"


/**
 * palin_check -  a function that checks if a singly linked has
 *   a palindrome in its values using recursion.
 * @head: pointer to the FIRST node of the list
 * @tail: pointer to point the LAST node of the list
 *
 * Return: 0 if list is NOT palindrome, 1 if palindrome
 */

int palin_check(listint_t **head, listint_t *tail)
{
/* if the end of the list in reached */
if (tail == NULL)
return (1);

/* using recursion to go throut the elements of the linked list */
/* one pointer moves from top to bottop, the other thus the opposit */
/* and we compare if the numbers are the same while moving */
if (palin_check(head, tail->next) && (*head)->n == tail->n)
{
*head = (*head)->next;
return (1);
}
  
return 0;
}


/**
 * is_palindrome -  a function that checks if a singly linked list
 *    is a palindrome.
 * @head: pointer to  the given list
 *
 * Return: 0 if list is NOT palindrome, 1 if palindrome
 */

int is_palindrome(listint_t **head)
{
int result;
  /* if list is empty, is palindrom */
if (*head == NULL || head == NULL)
  return (1);

  /* else check if its palindrom / return thre resulte */
result = palin_check(head, *head);

return (result);
}
