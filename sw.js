self.addEventListener('install', (e) => {
    console.log('アプリがインストールされました');
});

self.addEventListener('fetch', (e) => {
    // 今回は特にオフライン処理などは記述しません
});