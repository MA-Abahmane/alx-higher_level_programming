#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * check_cycle -  a function that checks if a singly linked 
 *    list has a cycle.
 * @list: given list pointer
 * Return: 1 if cycle found, 0 if not
 */

int check_cycle(listint_t *list)
{
listint_t *hare = list;
listint_t *tortus = list;

while (hare != NULL && hare->next != NULL)
{
/* one node at a time (tortus) */
tortus =  tortus->next;
/* two nodes at a time (hare) */
hare = hare->next->next;

/* if cycle found */
if (tortus == hare)
return (1);

}
  
return (0);
}
