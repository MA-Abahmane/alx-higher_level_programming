#include "lists.h"

/**
 * main -  a function that prints all the elements of a dlistint_t list.
 * @h: list to print its elements
 *
 * Return: the number of nodes
 */

size_t print_dlistint(const dlistint_t *h)
{
int count = 0;
const dlistint_t *ptr;

ptr = h;

while (ptr)
{
printf("%d\n",ptr->n);
ptr = ptr->next;
count ++;
}

return (count);
}