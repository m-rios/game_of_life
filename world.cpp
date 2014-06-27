#include "world.h"

world::world(int x, int y)
{
    for (int i = 0; i < x; ++i)
    {
        /* code */
    }
}

bool world::last(cell* cell)
{
    return cell->right == NULL && cell->lower == NULL;
}

void world::next(cell* current)
{
    if (current->right)
        current = current->right;
    else //end of line
        current = current->parent->lower;
}

void world::update()
{
    current = p_zero;
    while(!last(current))
    {
        current->alive = current->next;
        current = next(current);
    }

    current->alive = current->next;
}

void world::generate()
{
    cell* current = p_zero;
    int neighbours;
    
    while(1)
    {
        //count neighbours
        neighbours = 0;
        if (current->upper_left)
            if (current->upper_left->alive)
                neighbours++;
        if (current->upper)
            if (current->upper->alive)
                neighbours++;
        if (current->upper_right)
            if (current->upper_right->alive)
                neighbours++;
        if (current->right)
            if (current->right->alive)
                neighbours++;
        if (current->lower_right)
            if (current->lower_right->alive)
                neighbours++;
        if (current->lower)
            if (current->lower->alive)
                neighbours++;
        if (current->lower_left)
            if (current->lower_left->alive)
                neighbours++;
        if (current->left)
            if (current->left->alive)
                neighbours++;

        //apply gol rules
        if (neighbours < 2) //underpopulation
            current->next = false;
        else if (neighbours > 3) //overpopulation
            current->next = false;
        else //survive / reproduction
            current->next = true;

        //if current is last cell exit
        if (last(current))
            break;

        //get next cell
        next(current);
    }
    update();   
}