#include "cell.h"

#ifndef WORLD_H
#define WORLD_H

class world
{
private:
    cell* p_zero;
    bool last(cell* p_zero);
    void update();
    void next(cell* current);

public:
    world();
    ~world();
    void print();
    void generate();
};
#endif