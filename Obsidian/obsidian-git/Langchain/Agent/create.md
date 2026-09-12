`create_agent(`
  `model: str | BaseChatModel,`
  `tools: Sequence[BaseTool | Callable[..., Any] | dict[str, Any]] | None = None,`
  `*,`
  `system_prompt: str | SystemMessage | None = None,`
  `middleware: Sequence[AgentMiddleware[StateT_co, ContextT]] = (),`
  `response_format: ResponseFormat[ResponseT] | type[ResponseT] | dict[str, Any] | None = None,`
  `state_schema: type[AgentState[ResponseT]] | None = None,`
  `context_schema: type[ContextT] | None = None,`
  `checkpointer: Checkpointer | None = None,`
  `store: BaseStore | None = None,`
  `interrupt_before: list[str] | None = None,`
  `interrupt_after: list[str] | None = None,`
  `debug: bool = False,`
  `name: str | None = None,`
  `cache: BaseCache[Any] | None = None,`
  `transformers: Sequence[TransformerFactory] | None = None`
`) -> CompiledStateGraph[AgentState[ResponseT], ContextT, InputAgentState, OutputAgentState[ResponseT]]`