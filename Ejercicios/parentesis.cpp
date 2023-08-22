#include <bits/stdc++.h>
using namespace std;

string solve(){
    string cad;
    stack<char> par;
    stack<char> cor;

    for (int i = 0; i < cad.size(); i++)
    {
        if(cad[i]==')' && !par.empty()){
            par.pop();
        }
        else if(cad[i]==')'){
            return "NO";
        }else if(cad[i]=='('){
            par.push(cad[i]);
        }

        if (cad[i] == ']' && !cor.empty())
        {
            cor.pop();
        }
        else if (cad[i] == ']')
        {
            return "NO";
        }
        else if (cad[i] == '[')
        {
            cor.push(cad[i]);
        }
    }
    if(cor.empty() && par.empty()){
        return "YES";
    }
    else{
        return "NO";
    }
}
int main(){
    int n;
    cin >> n;
    while(n--){
        cout << solve() <<"\n";
    }
    return 0;
}