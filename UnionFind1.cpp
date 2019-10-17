#include <iostream>
#include <fstream>
#include <vector>
#include <set>
// #include <algorithm>
#include <utility>
using namespace std;

class UF {
private:
	vector< set<int> > *components;
public:
	UF() {
		components = new vector< set<int> >();
	}

	vector< set<int> >* getList() {
		return components;
	}

	bool Connected(int p, int q) {
		
		for (vector<set<int> >::iterator it = this->components->begin(); it != components->end(); it++) {
			if (it->find(p) != it->end()) {
				if (it->find(q) != it->end()) {
					return true;
				}
			}
			return false;
		}
	}

	void Union(int p, int q) {
		bool qFound = false;
		bool pFound = false;
		vector<set<int> >::iterator qLayer;
		
		if (this->Connected(p, q)) {
			return;
		}

		for (vector<set<int> >::iterator it = this->components->begin(); it != components->end(); it++) {
			if (it->find(q) != it->end()) {
				qLayer = it;
				qFound = true;
			}

			if (it->find(p) != it->end()) {
				pFound = true;
				if (qFound) {
					for (set<int>::iterator number = it->begin(); number != it->end(); number++) {
						qLayer->insert(*number);
					}
					this->components->erase(it);
				}
				else {
					it->insert(q);
				}
			}
		}
	}

	~UF() {
		for (auto line : *components) {
			line.clear();
		}
		
		components->clear();
		delete[] components;
	}
};

vector<pair<int, int> > inputFromFile(string fileName) {
	ifstream file_stream;
	int p, q;

	file_stream.open(fileName, std::ifstream::in);

	vector<pair<int, int> > numbers = vector<pair<int, int> >();

	while (!file_stream.eof()) {
		file_stream >> p;
		file_stream >> q;
		numbers.push_back(make_pair(p, q));
	}

	file_stream.close();
	return numbers;
}

int main()
{
	vector<pair<int, int> > numbers = inputFromFile("input.txt");
	UF union_find = UF();

	for (vector<pair<int, int> >::iterator it = numbers.begin(); it != numbers.end(); it++) {
		union_find.Union(it->first, it->second);
	}
	vector< set<int> > *result_union = union_find.getList();
	for (vector< set<int> >::iterator it = result_union->begin(); it != result_union->end(); it++)
	{
		std::cout << "subset:\n";
		for (set<int>::iterator set_it = it->begin(); set_it != it->end(); set_it++)
		{
			cout << (*set_it) << ", ";
		}
	}

	return 0;
}