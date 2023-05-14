#include "lists.h"

/**
 * is_palindrome -  a function that checks if a singly linked list
 *    is a palindrome.
 * @head: pointer to  the given list
 *
 * Return: 0 if list is NOT palindrome, 1 if palindrome
 */
int is_palindrome(listint_t **head)
{
int i = 0, j = 0, arr_size = 0;
  listint_t  *ptr;

  /* if list is empty, is palindrom */
  if (head == NULL)
    return 1;
  
  /* find out how many numbers in the list */
  ptr = *head;
  while (ptr != NULL)
    {
      arr_size++;
      ptr = ptr->next;
    }

  /* set array size */
  int *num_arr = NULL;
  num_arr = malloc(4 * arr_size);

  /* add each number to my array */
  ptr = *head;
  i = 0;
  while (ptr != NULL)
    {
      num_arr[i] = ptr->n;
      ptr = ptr->next;
      i++;
    }

  /* check if my array makes a palindrop */
  i = 0;
  j = (arr_size - 1);
  while (i < arr_size - 1 && j >= 0)
    {
      if (num_arr[i] != num_arr[j])
      {
        free(num_arr);
        return 0;
      }
      i++;
      j--;
    }

  free(num_arr);
  return 1;
}
