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
listint_t *next_node;
listint_t *node;
listint_t *ptr;
int count;

  /* creat new node */
node = malloc(sizeof(listint_t));
if (node == NULL)
return (NULL);

node->n = number;
node->next = NULL;
  
  /* find the nodes destination */
count = 0;
ptr = *head;
while (count != 4)
  {
ptr = ptr->next;
count++;
}

  /* instal the node in place */
next_node = ptr->next;
    
ptr->next = node;
node->next = next_node;
  
return (node);
}
