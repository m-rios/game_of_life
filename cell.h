
struct cell
{
    cell* upper_left;
    cell* upper;    
    cell* upper_right
    cell* right;
    cell* lower_right;
    cell* lower;
    cell* lower_left;
    cell* left;
    cell* parent;
    bool alive;
    bool next;
    bool modified;
};