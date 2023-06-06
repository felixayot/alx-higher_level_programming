#include "lists.h"
/**
 * insert_node - Prototype Function
 * Description: Inserts a number into a sorted singly-linked list.
 * @head: A pointer to the head of linked list.
 * @number: input int for insertion.
 * Return: the address of the new node, or NULL if it failed
 */
listint_t *insert_node(listint_t **head, int number)
{
listint_t *newNode = createNode(number);
if (newNode == NULL)
{
return (NULL);
}
if (*head == NULL || number < (*head)->n)
{
newNode->next = *head;
*head = newNode;
}
else
{
listint_t *current = *head;
while (current->next != NULL && current->next->n < number)
{
current = current->next;
}
newNode->next = current->next;
current->next = newNode;
}
return (newNode);
}
/**
 * createNode - Function prototype
 * Description: Creates new node
 * @number: input int for insertion.
 * Return: the address of the new node, or NULL if it failed
 */
listint_t *createNode(int number)
{
listint_t *newNode = (listint_t *)malloc(sizeof(listint_t));
if (newNode == NULL)
{
printf("Memory allocation failed.\n");
return (NULL);
}
{
newNode->n = number;
newNode->next = NULL;
return (newNode);
}
}
