class Solution {
    public:
        vector<vector<int>> updateMatrix(vector<vector<int>>& mat) {
            int n = mat.size();
            int m = mat[0].size();
    
            vector<vector<int>> vis(n, vector<int> (m, 0));
            vector<vector<int>> dis(n, vector<int> (m, 0));
            
            queue<pair<pair<int, int>, int>> q;
    
            for(int i=0; i<n; i++){
                for(int j=0; j<m; j++){
                    if(mat[i][j] == 0){
                        q.push({{i, j}, 0});
                        vis[i][j] = 1;
                    }
                }
            }
            int rdir[] = {-1, 0, 1, 0};
            int cdir[] = {0, 1, 0, -1};
            while(!q.empty()){
                auto node = q.front();
                q.pop();
                int row = node.first.first;
                int col = node.first.second;
                int step = node.second;
    
                dis[row][col] = step;
    
                for(int i=0; i<4; i++){
                    int nr = row + rdir[i];
                    int nc = col + cdir[i];
    
                    if(nr>=0 && nr <n && nc>=0 && nc<m && vis[nr][nc] ==0 ){
                        vis[nr][nc] = 1;
                        q.push({{nr, nc}, step+1});
                    }
                }
            }
    
            return dis;
        }
    };