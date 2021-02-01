//当前代码编辑器所打开的文件，为空则为新建文件
var g_model = null;
var g_filename = "";
//编辑器实例
var g_editor = null;
var deco_list = [];// 

var test_comp = "import";

var autocompAPIs = {"python":
    {
        "keywords":[],
        "functions":[],
        "variables":[]
    }

}
//初始化编辑器
function init_editor(layoutid, code_str) {
    if (g_editor)
        return;
    //初始化编辑器
    require.config(
        {
            paths: { 'vs': 'monaco-editor-0.16.2/package/min/vs' },
            'vs/nls': { availableLanguages: { '*': 'zh-cn' } }
        }
    );
    require(['vs/editor/editor.main'], function () {
        g_editor = monaco.editor.create(
            document.getElementById(layoutid),
            {
                language: 'sql',             //程序语言
                theme: 'vs-dark',               //界面主题
                value: code_str,                //初始文本内容
                automaticLayout: true,          //随布局Element自动调整大小                        
                minimap: { enabled: true },       //代码略缩图
                fontSize: 24,                   //字体大小
                //wordWrap: "on",               //自动换行，注意大小写
                //wrappingIndent: "indent",     //自动缩进
                //glyphMargin: true,            //字形边缘
                //useTabStops: false,           //tab键停留
                //selectOnLineNumbers: true,    //单击行号选中该行
                //roundedSelection: false,      //
                //readOnly: false,              // 只读
                //cursorStyle: 'line',          //光标样式
                //automaticLayout: false,       //自动布局
                //autoIndent:true,              //自动布局
                //quickSuggestionsDelay: 500,   //代码提示延时
                glyphMargin: true
            }
        );
        
        var keyBindingSave = g_editor.addCommand(monaco.KeyCode.KEY_S|monaco.KeyMod.CtrlCmd, function() {
            on_save(g_filename,g_editor.getValue());
            test_comp = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa";
        });
        
        var deco_list= [// 通过这个可以进行标记的添加和删除。
            {
                range: new monaco.Range(3, 1, 3, 1),
                options: {
                    isWholeLine: true,
                    className: 'myContentClass',
                    glyphMarginClassName: 'glyphMarginBreakPoint'
                }
            }, {
                range: new monaco.Range(4, 1, 4, 1),
                options: {
                    isWholeLine: true,
                    className: 'myContentClass',
                    glyphMarginClassName: 'glyphMarginBreakPoint'
                }
            }
        ]
//        add_tab("Untitled-1", "");
        console.log(delete_marker(12));
        var decorations = g_editor.deltaDecorations([], deco_list);
        console.log(deco_list,deco_list[0].range.startLineNumber)//获取注释的开始时的行数。
        registerCompletions();
        registerCompletions2();
    });



    //自适应大小，可以不要
    window.onresize = editor_layout;
    //编辑器加载成功后创建websocket连接
    window.onload = init_webskt;
}



function init_webskt(){
    console.log("web socket initialized!!")
}

//自适应窗口大小
function editor_layout() {
    if (g_editor)
        g_editor.layout()
}

//设置主题风格 theme:vs-dark vs hc-black, fontsize:S M L XL XXL
function set_theme(theme, fontsize) {
    monaco.editor.setTheme(theme);

    const sizes = ['S', 'M', 'L', 'XL', 'XXL'];
    ind = sizes.indexOf(fontsize);
    if (ind < 0)
        return;
    //monaco.editor.FontInfo.fontSize = 24 * (1 + ind * 0.25)
}

//设置代码文件
function load_file(file, txt) {
    g_filename = file;
    g_editor.setValue(txt);
}

//保存代码到本地文件, 第一行为文件名, 文件名如果为空在在python端弹出保存对话框
function save_file(reqid, file) {
    fname = file;
    if (fname == "")
        fname = g_filename;
    data = {
        'cmd': 'savefile_rsp',
        'reqid': reqid,
        'file': fname,
        'txt': g_editor.getValue(),
        'errtxt': ''
    }
    senddata(data);
}


//////////////////////////////////////////////////////////////////////////////
///标签栏管理
//////////////////////////////////////////////////////////////////////////////
// == 值比较  === 类型比较 $(id) ---->  document.getElementById(id)
function $(id) {
    return typeof id === 'string' ? document.getElementById(id) : id;
}

//全局字典
var datas = new Array();

// 当前标签
var currtab = ""

// 切换标签
function switch_tab(newtab) {
    if (newtab == currtab)
        return;

    var tab = $(newtab.toString());
    if (!tab && newtab != "")
        return;

    if (tab)
        tab.className = 'current';
    datas[currtab] = g_editor.getValue();
    load_file(newtab, tab ? datas[newtab] : '');

    tab = $(currtab.toString())
    if (tab)
        tab.className = '';

    currtab = newtab;
    // g_filename = currtab.id;
}

function open(name,value){
}

// 添加标签
function add_tab(name, value) {
    if (name == "" || datas[name])
        return;

    //新建标签
    var tab = document.createElement("li");
    tab.id = name;
    tab.innerHTML = name.substr(name.lastIndexOf('/') + 1);

    //新建关闭按钮
    var btn = document.createElement("a");
    btn.href = "#";
    btn.innerHTML = "x";

    //添加按钮到标签上
    tab.appendChild(btn);
    //添加按钮到标签栏上
    $('tabs').appendChild(tab);

    //设置标签和按钮的单击事件
    tab.onclick = function () {
        switch_tab(this.id);
    }
    btn.onclick = function () {
        var tab = this.parentNode;
        if (tab.className == 'current') {
            var _tab = tab.nextElementSibling;
            if (!_tab)
                _tab = tab.previousElementSibling;
            switch_tab(_tab ? _tab.id : '');
        }
        delete datas[tab.id];
        tab.remove();
    }

    //添加标签关联的数据
    datas[name] = value;
    //切换到新标签
    switch_tab(name);
}

function update_tab(name, value) {
    var tab = $(currtab.toString());
    tab.id = name;
    tab.innerHTML = name.substr(name.lastIndexOf('/') + 1);

    var btn = document.createElement("a");
    btn.href = "#";
    btn.innerHTML = "x";

    //添加按钮到标签上
    tab.appendChild(btn);
    //添加按钮到标签栏上
    $('tabs').appendChild(tab);

    //设置标签和按钮的单击事件
    tab.onclick = function () {
        switch_tab(this.id);
    }
    btn.onclick = function () {
        var tab = this.parentNode;
        if (tab.className == 'current') {
            var _tab = tab.nextElementSibling;
            if (!_tab)
                _tab = tab.previousElementSibling;
            switch_tab(_tab ? _tab.id : '');
        }
        delete datas[tab.id];
        tab.remove();
    }

    currtab = name;
}



function createDependencyProposals(range) {
    // returning a static list of proposals, not even looking at the prefix (filtering is done by the Monaco editor),
    // here you could do a server side lookup
    // 这个函数每次都会被调用一次！！！！！！
    return [
        {
            label: 'import',
            kind: monaco.languages.CompletionItemKind.Keyword,
            documentation: "The Lodash library exported as Node.js modules.",
            insertText: test_comp,
            range: range
        },
        {
            label: 'num',
            kind: monaco.languages.CompletionItemKind.Function,
            documentation: "Fast, unopinionated, minimalist web framework",
            insertText: '"express": "*"',
            range: range
        },
        {
            label: '"mkdirp"',
            kind: monaco.languages.CompletionItemKind.Function,
            documentation: "Recursively mkdir, like <code>mkdir -p</code>",
            insertText: '"mkdirp": "*"',
            range: range
        },
        {
            label: '"my-third-party-library"',
            kind: monaco.languages.CompletionItemKind.Function,
            documentation: "Describe your library here",
            insertText: '"${1:my-third-party-library}": "${2:1.2.3}"',
            insertTextRules: monaco.languages.CompletionItemInsertTextRule.InsertAsSnippet,
            range: range
        }
    ];
}


function createDependencyProposals2(range) {
    // returning a static list of proposals, not even looking at the prefix (filtering is done by the Monaco editor),
    // here you could do a server side lookup
    return [
        {
            label: 'for',
            kind: monaco.languages.CompletionItemKind.Keyword,
            documentation: "The Lodash library exported as Node.js modules.",
            insertText: 'for',
            range: range
        },
        {
            label: 'num',
            kind: monaco.languages.CompletionItemKind.Function,
            documentation: "Fast, unopinionated, minimalist web framework",
            insertText: '"express": "*"',
            range: range
        },
        {
            label: '"mkdirp"',
            kind: monaco.languages.CompletionItemKind.Function,
            documentation: "Recursively mkdir, like <code>mkdir -p</code>",
            insertText: '"mkdirp": "*"',
            range: range
        },
        {
            label: '"my-third-party-library"',
            kind: monaco.languages.CompletionItemKind.Function,
            documentation: "Describe your library here",
            insertText: '"${1:my-third-party-library}": "${2:1.2.3}"',
            insertTextRules: monaco.languages.CompletionItemInsertTextRule.InsertAsSnippet,
            range: range
        }
    ];
}

function registerCompletions(){
    monaco.languages.registerCompletionItemProvider('python', {
        provideCompletionItems: function(model, position) {
            // find out if we are completing a property in the 'dependencies' object.
            var textUntilPosition = model.getValueInRange({startLineNumber: 1, startColumn: 1, endLineNumber: position.lineNumber, endColumn: position.column});
            var match = textUntilPosition.match(".");//"dependencies"\s*:\s*\{\s*("[^"]*"\s*:\s*"[^"]*"\s*,\s*)*([^"]*)?$/);
            if (!match) {
                return { suggestions: [] };
            }
            var word = model.getWordUntilPosition(position);
            var range = {
                startLineNumber: position.lineNumber,
                endLineNumber: position.lineNumber,
                startColumn: word.startColumn,
                endColumn: word.endColumn
            };
            return {
                suggestions: createDependencyProposals(range)
            };
        }
    });
}


function registerCompletions2(){
    monaco.languages.registerCompletionItemProvider('python', {
        provideCompletionItems: function(model, position) {
            // find out if we are completing a property in the 'dependencies' object.
            var textUntilPosition = model.getValueInRange({startLineNumber: 1, startColumn: 1, endLineNumber: position.lineNumber, endColumn: position.column});
            var match = textUntilPosition.match(".");//"dependencies"\s*:\s*\{\s*("[^"]*"\s*:\s*"[^"]*"\s*,\s*)*([^"]*)?$/);
            if (!match) {
                return { suggestions: [] };
            }
            var word = model.getWordUntilPosition(position);
            var range = {
                startLineNumber: position.lineNumber,
                endLineNumber: position.lineNumber,
                startColumn: word.startColumn,
                endColumn: word.endColumn
            };
            return {
                suggestions: createDependencyProposals2(range)
            };
        }
    });
}