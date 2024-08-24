console.log("JavaScript carregado!");  // Este console.log verifica se o script está carregado

// Seleciona os elementos do DOM
const addTaskButton = document.getElementById('add-task');
const taskInput = document.getElementById('new-task');
const taskList = document.getElementById('task-list');

// Verifica se os elementos foram encontrados
console.log(addTaskButton, taskInput, taskList); // Isso ajuda a verificar se os elementos estão sendo encontrados

// Função para adicionar uma nova tarefa
function addTask() {
    const taskText = taskInput.value.trim(); // Pega o valor do input e remove espaços extras
    if (taskText === '') {
        alert('Por favor, insira uma tarefa.');
        return;
    }

    // Cria um novo elemento de lista para a tarefa
    const li = document.createElement('li');
    li.textContent = taskText;

    // Adiciona a funcionalidade de marcar como concluída ao clicar na tarefa
    li.addEventListener('click', function() {
        li.classList.toggle('completed');
    });

    // Cria um botão de excluir para a tarefa
    const deleteButton = document.createElement('button');
    deleteButton.textContent = 'Excluir';
    deleteButton.onclick = function() {
        taskList.removeChild(li);
    };

    // Adiciona o botão de excluir ao elemento de lista
    li.appendChild(deleteButton);

    // Adiciona o elemento de lista (li) ao elemento de lista não ordenada (ul)
    taskList.appendChild(li);

    // Limpa o input após adicionar a tarefa
    taskInput.value = '';
}

// Adiciona o evento de clique ao botão de adicionar tarefa
addTaskButton.addEventListener('click', addTask);
