#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * insert_node - a function that inserts a number into a sorted singly linked list.
 * @head: pointer to pointer of first node of listint_t list.
 * @number: integer to be included in new node.
 *
 * Return: address of the new element or NULL if it fails
 */

listint_t *insert_node(listint_t **head, int number)
{
listint_t *node;
listint_t *ptr;
int count;

  /* creat new node */
node = malloc(sizeof(listint_t));
if (node == NULL)
  return (NULL);

node->n = number;
node->next = NULL;

ptr = *head;

  /* if: the head node in it larger than our node */
if (node->n < ptr->n || ptr == NULL)
{
  node->next = ptr;
  *head = node;
  return (*head);
}

  /* else: find for the destinations of the node*/
while (ptr)
{
  /* if reached end of list or destination found: set the node*/
  if (node->n < ptr->next->n || ptr->next == NULL)
    {
      node->next = ptr->next;
      ptr->next = node;
      return (ptr);
    }
    ptr = ptr->next;
}

return (NULL);
}
